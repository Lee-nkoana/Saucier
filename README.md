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

4. ## Install model

   Install Ollama: https://ollama.com

   ```bash
   ollama run mistral
   ```

5. ## How to run the app
   ```bash
   cd backend
   flask run
   ```

   or 

   ```bash
   cd backend
   python app.py
   ```

## 🧑‍💻 Contributing

Contributions are more than welcome!
If you have ideas, issues, or want to contribute code, feel free to open a pull request or issue.

Refer to the CONTRIBUTIONS.md for git commit message structures.

## 📂 Project Structure

```
   Saucier/
   ├── CONTRIBUTIONS.md          # Contribution guidelines
   ├── README.md                 # This file
   ├── requirements.txt          # Python dependencies
   ├── backend/                  # Flask backend
   │   ├── app.py                # App entrypoint
   │   ├── __init__.py
   │   ├── api/                  # API route modules
   │   │   ├── auth.py
   │   │   ├── login.py
   │   │   ├── mealPrep.py
   │   │   ├── posts.py
   │   │   ├── recipes.py
   │   │   └── register.py
   │   └── models/               # Backend data models
   │       ├── posts.py
   │       ├── prep.py
   │       ├── recipes.py
   │       └── users.py
   └── frontend/                 # Frontend assets and templates
      ├── static/
      │   ├── css/
      │   │   ├── animations.css
      │   │   ├── explore.css
      │   │   ├── index.css
      │   │   ├── login.css
      │   │   ├── profile.css
      │   │   ├── register.css
      │   │   └── styles.css
      │   ├── images/
      │   └── js/
      │       ├── animations.js
      │       ├── api_connector.js
      │       ├── auth_user.js
      │       ├── explore.js
      │       └── profile.js
      └── templates/
         ├── chat.html
         ├── explore.html
         ├── index.html
         ├── login.html
         ├── profile.html
         └── register.html
```
