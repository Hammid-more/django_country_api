# Citizens API (Django REST Framework)

A simple REST API for managing citizen records built with **Django & Django REST Framework**.

## 🚀 Features
- Create a citizen
- Retrieve all citizens
- Retrieve individual citizen
- Update citizen record
- Delete citizen record

---

## 📦 Tech Stack
- Python 3.x
- Django
- Django REST Framework
- SQLite (default) / MySQL (optional)

---

## 📁 Project Structure

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repo
```bash
git clone https://github.com/your-username/django-country-api.git


cd django-country-api


python -m venv venv


venv\Scripts\activate        # Windows


pip install -r requirements.txt


python manage.py migrate


python manage.py runserver


API runs at:
http://127.0.0.1:8000/


🧪 API Endpoints
✅ Create Citizen (POST)

POST /api/citizens/

Body (JSON)

{
  "first_name": "Hammed",
  "father_name": "Lawal",
  "mother_name": "Amina",
  "home_town": "Lagos",
  "gender": "Male"
}


✅ Get All Citizens (GET)

GET /api/citizens/

✅ Get Citizen by ID (GET)

GET /api/citizens/<id>/

✅ Update Citizen (PUT)

PUT /api/citizens/<id>/

✅ Delete Citizen (DELETE)

DELETE /api/citizens/<id>/

🧰 Testing with Postman

Open Postman

Paste your endpoint URL

Select method (GET, POST, PUT, DELETE)

For POST/PUT — choose Body > Raw > JSON




