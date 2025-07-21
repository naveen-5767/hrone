Sure! Here's your **complete `README.md` file content** — written fully in **Markdown language**, ready to paste or save directly:

---

```markdown
# 📦 Sample Backend API using FastAPI and MongoDB

This is a sample backend application built with **FastAPI** and **MongoDB**, which serves mock data for `users`, `products`, and `orders` collections from a MongoDB Atlas cluster.

---

## 🚀 Features

- ✅ Built using **FastAPI** for high-performance APIs
- ✅ Connects to **MongoDB Atlas** using `pymongo`
- ✅ Supports `.env` for secure and flexible configuration
- ✅ Exposes REST endpoints for:
  - `/api/users`
  - `/api/products`
  - `/api/orders`

---

## 📁 Project Structure

```

final/
│
├── main.py          # FastAPI application code
├── .env             # MongoDB URI (optional)
└── README.md        # Project documentation

````

---

## 🔧 Setup Instructions

### 1. ✅ Clone the Repository

```bash
git clone <your-repo-url>
cd final
````

### 2. 🐍 Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 3. 📦 Install Dependencies

```bash
pip install fastapi pymongo "uvicorn[standard]" python-dotenv
```

---

## 🔐 Environment Variables

You can optionally use a `.env` file to store your MongoDB URI:

**Create `.env` in the root folder:**

```
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority&appName=MyAPICluster
```

If no `.env` is found, it will fallback to the hardcoded URI in `main.py`.

---

## ▶️ Run the Application

Run the app using Uvicorn:

```bash
uvicorn main:app --reload
```

### Visit:

* Base URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* API Docs (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 API Endpoints

| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| GET    | `/`             | Welcome message     |
| GET    | `/api/users`    | Returns 10 users    |
| GET    | `/api/products` | Returns 10 products |
| GET    | `/api/orders`   | Returns 10 orders   |

---

## 🧪 Sample Output Format

Sample mock JSON output from each endpoint:

### `/api/users`

```json
[
  {
    "username": "john_doe",
    "email": "john@example.com"
  },
  {
    "username": "jane_doe",
    "email": "jane@example.com"
  }
]
```

### `/api/products`

```json
[
  {
    "name": "iPhone 14",
    "price": 999.99
  },
  {
    "name": "MacBook Pro",
    "price": 1999.00
  }
]
```

### `/api/orders`

```json
[
  {
    "user": "john_doe",
    "product": "iPhone 14",
    "status": "shipped"
  },
  {
    "user": "jane_doe",
    "product": "MacBook Pro",
    "status": "pending"
  }
]
```

---

## 🛠 Dependencies

* **FastAPI** – API framework
* **Uvicorn** – ASGI server
* **pymongo** – MongoDB Python client
* **python-dotenv** – Load environment variables

---

## 🧑‍💻 Author

**Naveen**
Made with ❤️ for HROne Backend Task

---

## 🛡 License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

```

---

Let me know if you'd like me to generate and send the `.md` file as a downloadable attachment too!
```
