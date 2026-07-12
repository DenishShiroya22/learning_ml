{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyMCi8qDyp0Ue2JrQ5+9FRsg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DenishShiroya22/learning_ml/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XmZldzxNqb9H",
        "outputId": "c05b6ac0-ca11-4643-f18f-39b207d01fa5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-07-12 09:44:17.973 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.974 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.975 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.975 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.976 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.976 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.978 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.979 No runtime found, using MemoryCacheStorageManager\n",
            "2026-07-12 09:44:17.982 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.985 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.985 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-12 09:44:17.986 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "# 1. Setup the web page\n",
        "st.set_page_config(page_title=\"Score Predictor\", page_icon=\"🎓\")\n",
        "st.title(\"🎓 Student Exam Score Predictor\")\n",
        "st.write(\"Welcome to my first Machine Learning Web App! Enter your study hours below to see your predicted score.\")\n",
        "\n",
        "# 2. Load the data and train the model automatically\n",
        "# (We use @st.cache_data so it only trains once and runs super fast!)\n",
        "@st.cache_data\n",
        "def train_model():\n",
        "    # NOTE: Change 'student_scores.csv' if your dataset has a different name!\n",
        "\n",
        "    df = pd.read_csv(\"data.csv\",usecols=['hours_studied','exam_score'])\n",
        "    df = df.rename(columns={\n",
        "    'hours_studied':'Hours',\n",
        "    'exam_score':'Scores'\n",
        "    })\n",
        "\n",
        "    # We use the clean data just like in your Jupyter notebook\n",
        "    X = df[['Hours']]\n",
        "    y = df['Scores']\n",
        "\n",
        "    model = LinearRegression()\n",
        "    model.fit(X, y)\n",
        "    return model\n",
        "\n",
        "try:\n",
        "    # Train the model\n",
        "    model = train_model()\n",
        "\n",
        "    # 3. Create the interactive user input\n",
        "    hours = st.number_input(\"How many hours did you study?\", min_value=0.0, max_value=24.0, value=5.0, step=0.5)\n",
        "\n",
        "    # 4. Make the prediction when they click the button\n",
        "    if st.button(\"Predict My Score!\"):\n",
        "        prediction = model.predict([[hours]])\n",
        "        final_score = min(prediction[0], 100.0) # Cap the score at 100%\n",
        "\n",
        "        st.success(f\"📈 If you study for {hours} hours, your predicted score is: **{final_score:.2f}%**\")\n",
        "        st.balloons() # This adds a fun balloon animation on the screen!\n",
        "\n",
        "except FileNotFoundError:\n",
        "    st.error(\"Oops! I can't find the CSV file. Make sure your data file is uploaded to GitHub and named correctly!\")"
      ]
    }
  ]
}