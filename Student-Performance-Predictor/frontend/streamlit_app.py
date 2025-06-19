import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="🎓 Student Grade Predictor", page_icon="📚", layout="centered")
st.title("🎓 Student Grade Predictor")
st.markdown("""
Welcome to the smart student performance prediction app! 
Fill in the form below to predict a student's final grade (G3).
""")

with st.form("student_form"):
    st.subheader("📋 Student Full Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        school = st.selectbox("School", ["GP", "MS"])
        sex = st.selectbox("Sex", ["F", "M"])
        age = st.slider("Age", 15, 22, 17)
        address = st.selectbox("Address", ["U", "R"])
        famsize = st.selectbox("Family Size", ["LE3", "GT3"])
        Pstatus = st.selectbox("Parent Cohabitation", ["T", "A"])
        Medu = st.slider("Mother's Education (0-4)", 0, 4)
        Fedu = st.slider("Father's Education (0-4)", 0, 4)
        Mjob = st.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
        Fjob = st.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])

    with col2:
        reason = st.selectbox("Reason to Choose School", ["home", "reputation", "course", "other"])
        guardian = st.selectbox("Guardian", ["mother", "father", "other"])
        traveltime = st.slider("Travel Time (1-4)", 1, 4)
        studytime = st.slider("Study Time (1-4)", 1, 4)
        failures = st.slider("Past Class Failures", 0, 4)
        schoolsup = st.selectbox("Extra School Support", ["yes", "no"])
        famsup = st.selectbox("Family Educational Support", ["yes", "no"])
        paid = st.selectbox("Paid Classes", ["yes", "no"])
        activities = st.selectbox("Extracurricular Activities", ["yes", "no"])
        nursery = st.selectbox("Attended Nursery School", ["yes", "no"])

    with col3:
        higher = st.selectbox("Wants Higher Education", ["yes", "no"])
        internet = st.selectbox("Internet Access", ["yes", "no"])
        romantic = st.selectbox("In Romantic Relationship", ["yes", "no"])
        famrel = st.slider("Family Relationship Quality (1-5)", 1, 5)
        freetime = st.slider("Free Time (1-5)", 1, 5)
        goout = st.slider("Going Out Frequency (1-5)", 1, 5)
        Dalc = st.slider("Workday Alcohol Consumption (1-5)", 1, 5)
        Walc = st.slider("Weekend Alcohol Consumption (1-5)", 1, 5)
        health = st.slider("Health Status (1-5)", 1, 5)
        absences = st.number_input("Number of Absences", 0, 100, 4)
        G1 = st.slider("First Period Grade (G1)", 0, 20)
        G2 = st.slider("Second Period Grade (G2)", 0, 20)

    submitted = st.form_submit_button("🔍 Predict Grade")

if submitted:
    average_grade = (G1 + G2) / 2
    with st.spinner("Predicting grade..."):
        input_data = {
            "school": school,
            "sex": sex,
            "age": age,
            "address": address,
            "famsize": famsize,
            "Pstatus": Pstatus,
            "Medu": Medu,
            "Fedu": Fedu,
            "Mjob": Mjob,
            "Fjob": Fjob,
            "reason": reason,
            "guardian": guardian,
            "traveltime": traveltime,
            "studytime": studytime,
            "failures": failures,
            "schoolsup": schoolsup,
            "famsup": famsup,
            "paid": paid,
            "activities": activities,
            "nursery": nursery,
            "higher": higher,
            "internet": internet,
            "romantic": romantic,
            "famrel": famrel,
            "freetime": freetime,
            "goout": goout,
            "Dalc": Dalc,
            "Walc": Walc,
            "health": health,
            "absences": absences,
            "G1": G1,
            "G2": G2,
            "average_grade": average_grade
        }

        try:
            response = requests.post("http://127.0.0.1:8000/api/predict/", json=input_data)
            if response.status_code == 200:
                prediction = response.json()['predicted_grade']
                st.success(f"📈 Predicted Final Grade (G3): **{prediction}**")

                with st.expander("📦 Raw Input Data"):
                    st.json(input_data)
                    st.caption(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                st.error(f"❌ Prediction failed: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Could not connect to API: {e}")

st.markdown("---")
st.caption("Developed by Hamza | Powered by Django + Supabase + Streamlit")
