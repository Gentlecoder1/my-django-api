# API Documentation

## Base URL

- Local: `http://127.0.0.1:8000/`

---

## Endpoints

### 1. Signup

- **URL:** `/signup/`
- **Method:** `POST`
- **Description:** Register a new user.
- **Request Body (JSON):**
  ```json
  {
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password"
  }
  ```
- **Response (201 Created):**
  ```json
  {
    "username": "your_username",
    "email": "your_email@example.com"
  }
  ```
- **Response (400 Bad Request):**
  ```json
  {
    "field_name": ["error message"]
  }
  ```

---

### 2. Login

- **URL:** `/login/`
- **Method:** `POST`
- **Description:** Authenticate a user with username and password.
- **Request Body (JSON):**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "message": "Login successful"
  }
  ```
- **Response (400 Bad Request):**
  ```json
  {
    "error": "Invalid credentials"
  }
  ```

---

## Notes

- All requests and responses use JSON format.
- Make sure to include the trailing slash (`/`) in endpoint URLs.
- For production, replace the base URL with your deployed server address.

---

## Example Usage (with curl)

**Signup:**

```sh
curl -X POST http://127.0.0.1:8000/signup/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpassword"}'
```

**Login:**

```sh
curl -X POST http://127.0.0.1:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'
```
