# Basic Python Concepts

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Function

def greet(user):
    print(f"OK {user} Thanks for learning stay tuned for more !")

# Conditional Statements
print("\nIF ELSE")
if age < 18:
    print("You are a minor")
else:
    print("You are an adult")

# Loop

print("\nLet's practice Loops")
for i in range(1,6):
    print(f"Loop iteration {i}:, Keep going {name}")

#End of Program
greet(name)