import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Setup the web page
st.set_page_config(page_title="Score Predictor", page_icon="🎓")
st.title("🎓 Student Exam Score Predictor")
st.write("Welcome to my first Machine Learning Web App! Enter your study hours below to see your predicted score.")

# 2. Load the data and train the model automatically
# (We use @st.cache_data so it only trains once and runs super fast!)
@st.cache_data 
def train_model():
    # NOTE: Change 'student_scores.csv' if your dataset has a different name!
    
    df = pd.read_csv("data.csv",usecols=['hours_studied','exam_score'])
    df = df.rename(columns={
    'hours_studied':'Hours',
    'exam_score':'Scores'
    })
    
    # We use the clean data just like in your Jupyter notebook
    X = df[['Hours']] 
    y = df['Scores']
    
    model = LinearRegression()
    model.fit(X, y)
    return model

try:
    # Train the model
    model = train_model()
    
    # 3. Create the interactive user input
    hours = st.number_input("How many hours did you study per day?", min_value=0.0, max_value=24.0, value=5.0, step=0.5)
    
    # 4. Make the prediction when they click the button
    if st.button("Predict My Score!"):
        prediction = model.predict([[hours]])
        final_score = min(prediction[0], 100.0) # Cap the score at 100%
        
        st.success(f"📈 If you study for {hours} hours, your predicted score is: **{final_score:.2f} out of 50**")
        st.balloons() # This adds a fun balloon animation on the screen!

except FileNotFoundError:
    st.error("Oops! I can't find the CSV file. Make sure your data file is uploaded to GitHub and named correctly!")
