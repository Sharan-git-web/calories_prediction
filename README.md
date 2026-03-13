# 🔥 AI Calories Burn Prediction App

A Machine Learning web application that predicts the number of **calories burned during exercise** based on body metrics and workout parameters.

The application uses a trained ML model and an interactive web interface to provide real-time predictions.

🌐 **Live Demo:**
https://calorieburns-predictor.streamlit.app/

---

# 🚀 Features

* Predict calories burned during workouts
* Interactive user interface
* Real-time machine learning predictions
* BMI calculation with health feedback
* Workout intensity classification
* Simple and user-friendly design

---

# 📊 Input Parameters

The model uses the following inputs:

| Parameter         | Description                     |
| ----------------- | ------------------------------- |
| Gender            | Male / Female                   |
| Age               | Age of the person               |
| Height            | Height in cm                    |
| Weight            | Weight in kg                    |
| Exercise Duration | Duration of workout (minutes)   |
| Heart Rate        | Heart rate during exercise      |
| Body Temperature  | Body temperature during workout |

---

# 🧠 Machine Learning Model

The model was trained using exercise and calories datasets.

**Workflow:**

1. Data preprocessing
2. Feature engineering
3. Model training
4. Model evaluation
5. Model deployment

The trained model is saved using **Pickle** and loaded in the web app for predictions.

---

# 🖥️ Tech Stack

* Python
* Streamlit
* NumPy
* Scikit-learn
* Pandas
* Pickle

---

# 📂 Project Structure

```
calories_prediction/
│
├── app.py
├── calories_model.pkl
├── calories_prediction.ipynb
├── calories.csv
├── exercise.csv
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/calories_prediction.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

# 📈 How It Works

1. User enters workout and body details.
2. Data is converted into numerical format.
3. The trained ML model processes the input.
4. The system predicts calories burned.
5. The app displays results with workout intensity feedback.

---

# 🎯 Future Improvements

* Add data visualization charts
* Add workout recommendations
* Deploy with a custom domain
* Add user progress tracking
* Improve model accuracy

---

# 👨‍💻 Author

**Valurothu Sharan**

Computer Science Engineering Student
Interested in AI, Machine Learning, and Full-Stack Development.

---
