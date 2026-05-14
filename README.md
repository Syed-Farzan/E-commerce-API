# Mini E-Commerce REST API 🛒

A RESTful backend API for a mini e-commerce platform built with FastAPI and Python.

The project focuses on clean API design, structured routing, request validation, error handling, and basic inventory management. It currently uses an in-memory datastore for simplicity while keeping the architecture ready for future database integration.

---

## 🚀 Features

- User and product management APIs
- Structured routing using FastAPI routers
- Request and response validation with Pydantic V2
- Partial updates using `exclude_unset=True`
- Inventory tracking with stock management
- Purchase endpoint with transaction logic
- Proper HTTP status codes and error handling
- Password fields excluded from API responses
- Category-based product filtering

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Language:** Python
- **Server:** Uvicorn
- **Validation:** Pydantic V2
- **Storage:** In-memory Python dictionaries
- **Environment Management:** python-dotenv

---

## 📂 Project Structure

```bash
app/
├── main.py
├── database.py
├── routers/
│   ├── users.py
│   └── products.py
├── models/
│   ├── users.py
│   └── products.py
├── routers/
│   ├── id_gen.py
```