# schema.py
import graphene
from graphene import String, Int, List, ObjectType, Field, Boolean
from employee_model import db, EmployeeModel

class Employee(ObjectType):
    id = Int()
    name = String()
    position = String()

class Query(ObjectType):
    employees = List(Employee)

    def resolve_employees(parent, info):
        return EmployeeModel.query.all()

class CreateEmployee(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        position = String(required=True)

    employee = Field(lambda: Employee)

    def mutate(parent, info, name, position):
        new_employee = EmployeeModel(name=name, position=position)
        db.session.add(new_employee)
        db.session.commit()
        return CreateEmployee(employee=new_employee)

class UpdateEmployee(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        position = String()

    employee = Field(lambda: Employee)

    def mutate(parent, info, id, name=None, position=None):
        emp = EmployeeModel.query.get(id)
        if emp is None:
            raise Exception("Employee not found")
        if name:
            emp.name = name
        if position:
            emp.position = position
        db.session.commit()
        return UpdateEmployee(employee=emp)

class DeleteEmployee(graphene.Mutation):
    class Arguments:
        id = Int(required=True)

    ok = Boolean()

    def mutate(parent, info, id):
        emp = EmployeeModel.query.get(id)
        if emp is None:
            raise Exception("Employee not found")
        db.session.delete(emp)
        db.session.commit()
        return DeleteEmployee(ok=True)

class Mutation(ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
