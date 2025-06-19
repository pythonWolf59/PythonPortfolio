from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import os
import pandas as pd
from .serializers import StudentDataSerializer
from .supabase_client import supabase

class PredictGradeView(APIView):
    def post(self, request):
        serializer = StudentDataSerializer(data=request.data)
        if serializer.is_valid():
            input_data = pd.DataFrame([serializer.validated_data])

            # Load model
            model_path = os.path.join(os.path.dirname(__file__), 'model', 'student_grade_predictor.pkl')
            model = joblib.load(model_path)

            # Encode categorical variables (same encoding as training)
            for col in input_data.select_dtypes(include='object').columns:
                input_data[col] = input_data[col].astype('category').cat.codes

            prediction = model.predict(input_data)[0]

            # Save prediction to Supabase
            supabase.table("predictions").insert({
                "input_data": serializer.validated_data,
                "predicted_grade": round(prediction, 2)
            }).execute()


            return Response({'predicted_grade': round(prediction, 2)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
