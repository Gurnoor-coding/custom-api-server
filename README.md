# Custom Task API Server

This project is a simple API server that provides **CRUD operations for tasks** using **FastAPI** and **SQLite**.

---

## 🔧 Functionality

The server exposes 4 API endpoints:

| Method | Endpoint            | Description         |
|--------|---------------------|---------------------|
| GET    | `/tasks/`           | Get all tasks       |
| POST   | `/tasks/`           | Create a new task   |
| PUT    | `/tasks/{id}`       | Update a task       |
| DELETE | `/tasks/{id}`       | Delete a task       |

Each task includes:
- `id`: integer (auto-incremented)
- `title`: string
- `completed`: boolean

---

## 🗃️ Database Used

The server uses **SQLite**, a lightweight, file-based database that stores data in a `tasks.db` file.

Database operations are handled using **SQLAlchemy ORM**.

---

## ▶️ How to Run the Server

### 1. Clone the Project
```bash
git clone https://github.com/your-username/custom_api_server.git
cd custom_api_server

## Testing & Coverage

This project uses `pytest` for unit, integration, and API testing. Coverage is measured using `pytest-cov`.

### Install Dependencies

```bash
pip install -r requirements.txt
pytest --cov=crud --cov=main --cov-report=term --cov-report=html

