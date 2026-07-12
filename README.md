Student Score Predictor: My First ML Web App 🎓

https://denishshiroya22-learning-ml-app-lozk1t.streamlit.app/
(Click the badge above to try the live web app!)

Overview

This project is my first practical application of Machine Learning! I built an interactive web application that uses a Linear Regression model to predict a student's final exam score based on the number of hours they studied.

The core question this project answers: For every additional hour a student studies, how many extra points can they expect to score on their exam?

Tools & Libraries Used

Python: The core programming language.

Pandas: Used for data cleaning and manipulation.

Scikit-Learn: Used to train and evaluate the Linear Regression model.

Streamlit: Used to turn the Python script into a live, interactive web application.

The Data

The dataset is a simple CSV containing two columns:

Hours: The number of hours a student studied.

Scores: The final percentage scored on the exam.

Key Findings & Results

After cleaning the data (handling outliers) and training the model, I evaluated its performance:

Coefficient (Slope): The model calculated a coefficient of 1.61. This means that a student's score increases by roughly 1.61 points for every extra hour they study.

Accuracy ($R^2$ Score): The model achieved an $R^2$ score of 0.64. This tells us that study time accounts for about 64% of the overall exam score, leaving 36% to be determined by other real-world factors.

How to Run This Project Locally

If you want to run the code on your own machine:

Clone this repository to your local machine.

Ensure you have Python installed, then install the required libraries:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py
