#  Django Expense Tracker API

A RESTful API built with Django and Django REST Framework for tracking income and expenses. Includes JWT authentication, role-based access, and tax calculations.

---

##  Features

-  JWT-based user authentication
-  Expense and income tracking
-  Flat and percentage tax calculation
-  Full CRUD operations
-  Token refresh functionality
-  User-based data access
-  Superuser access to all records
-  Paginated responses

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Manisha-Tmg/Django-Expense-Tracker
cd Django-Expense-Tracker
```
### 2. Create virtual environment & activate
```bash
python -m venv env
./env/scripts/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py migrate
```
### 5. Run the server
```bash
python manage.py runserver
```
----
Authentication Endpoints
| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/auth/register/` | Register a new user  |
| POST   | `/api/auth/login/`    | Obtain JWT tokens    |
| POST   | `/api/auth/refresh/`  | Refresh access token |


Authorization: Bearer <access_token>


Expense API Endpoints
| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| GET    | `/api/expenses/`      | List user's records      |
| POST   | `/api/expenses/`      | Create new record        |
| GET    | `/api/expenses/{id}/` | Retrieve specific record |
| PUT    | `/api/expenses/{id}/` | Update a record          |
| DELETE | `/api/expenses/{id}/` | Delete a record          |


Tax Calculation Logic
Flat Tax:
total = amount + tax

total = amount + tax

Percentage Tax:
total = amount + (amount * tax / 100)
---
###  Tech Stack

Python 3.8+
Django

Django REST Framework

Simple JWT

SQLite (development)
