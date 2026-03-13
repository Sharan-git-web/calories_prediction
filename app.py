import streamlit as st
import numpy as np
import pickle
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "calories_model.pkl")
model = pickle.load(open(model_path, "rb"))

# App title
st.title("🔥 Calories Burn Prediction App")

st.write(
    "This AI app predicts the number of calories burned during exercise "
    "based on body metrics and workout details."
)

# Layout
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    height = st.number_input("Height (cm)", value=175.0)

with col2:
    weight = st.number_input("Weight (kg)", value=70.0)
    duration = st.number_input("Exercise Duration (minutes)", value=30.0)
    heart_rate = st.number_input("Heart Rate", value=110.0)
    body_temp = st.number_input("Body Temperature", value=40.0)

# Convert gender
gender = 0 if gender == "Male" else 1

# BMI Calculation
bmi = weight / ((height/100) ** 2)

st.write(f"### 🧮 Your BMI: {bmi:.2f}")

if bmi < 18.5:
    st.warning("Underweight")
elif bmi < 25:
    st.success("Normal Weight")
elif bmi < 30:
    st.warning("Overweight")
else:
    st.error("Obese")

# Prediction
if st.button("Predict Calories Burned"):

    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

    prediction = model.predict(input_data)
    calories = prediction[0]

    st.success(f"🔥 Predicted Calories Burned: {calories:.2f}")

    if calories < 100:
        st.info("Light Workout 🔵")
    elif calories < 250:
        st.success("Moderate Workout 🟢")
    else:
        st.warning("High Intensity Workout 🔥")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit and Machine Learning")