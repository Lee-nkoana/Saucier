# 🥗 Saucier - Smart Meal Prep & Recipe Recommender

Saucier is a Python-powered **Flask web application** that helps users generate personalized meal preps, discover recipes, and get smart meal suggestions based on the ingredients, dietary preferences, and goals they input.

## 🚀 Features

- 🔍 **Smart Recipe Fetching** – Finds recipes from public APIs or a built-in database.
- 🧠 **Meal Suggestions** – Suggests balanced meals based on user goals (e.g. weight loss, bulking, keto).
- 🧺 **Meal Prepping** – Generates weekly meal plans and prep schedules.
- 📝 **Ingredient-Based Search** – Enter what you have at home and get suggestions for meals you can make.
- ✅ **Diet Filters** – Supports vegan, vegetarian, gluten-free, keto, etc.
- 💾 **User Profiles** – Save meal plans and preferences .

## 🧰 Tech Stack

- **Python**
- **Flask**
- **HTML / CSS / JavaScript**
- **PostgreSQL**
- **REST APIs**
- **Bootstrap / Tailwind CSS**

## 🔧 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/Lee-nkoana/saucier.git
   cd saucier
   ```

2. ## Create & activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. ## Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. ## How to run the app
   ```bash
   flask run
   ```

   or 

    ```bash
   python app.py
   ```

## 🧑‍💻 Contributing

Contributions are more than welcome!
If you have ideas, issues, or want to contribute code, feel free to open a pull request or issue.

## 📂 Project Structure

   ```plaintext
   saucier/
   │
   ├── app.py                 # Main Flask app entry point
   ├── requirements.txt       # Python dependencies
   ├── config.py              # Configurations (DB, API keys, etc.)
   │
   ├── /app                   # Application package
   │   ├── __init__.py
   │   ├── routes.py          # Flask routes / endpoints
   │   ├── models.py          # Database models
   │   ├── services/          # Logic for recipes, meal planning, AI integrations
   │   └── utils/             # Helper functions
   │
   ├── /templates             # HTML templates (Jinja2)
   │   ├── login.html
   │   ├── index.html
   │   ├── dashboard.html
   │   ├── meal_plan.html
   │   ├── Register.html
   │
   ├── /static                # Static files
   │   ├── css/
   │   ├── js/
   │   └── images/
   │
   └── /tests                 # Unit and integration tests

