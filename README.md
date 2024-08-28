# Flask API README

This README provides information about the Flask API, including its endpoints, functionality, and how to test it using Postman.

## Introduction

This Flask API provides a few endpoints to demonstrate basic routing and handling of HTTP methods. It includes routes for displaying messages and updating a global variable through a POST request.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Flask (`pip install flask`)

### Running the Application

1. Clone or download the repository containing the Flask application.
2. Navigate to the directory containing the `app.py` file (or whatever the file is named).
3. Run the application with the command:
    ```bash
    python app.py
    ```
4. The Flask application will start and listen on `http://127.0.0.1:5000/`.

## Endpoints

### 1. `GET /`

- **Description:** Returns a simple "Hello World!" message.
- **Response:** `Hello World!`

### 2. `GET /sit`

- **Description:** Returns a message about "SIT ROCKS!".
- **Response:** `SIT ROCKS!`

### 3. `GET /sheela`

- **Description:** Returns a message with Sheela's age, which is initially set to `26`.
- **Response:** `Sheela ki jawani! Umar 26`

### 4. `GET /sheela/<age>`

- **Description:** Returns a message with the provided age in the URL.
- **Response:** `Sheela ki umar <age>.`
- **Example Request:** `GET /sheela/30`
- **Example Response:** `Sheela ki umar 30.`

### 5. `POST /sheela`

- **Description:** Updates Sheela's age with the value provided in the POST request body.
- **Request Form Data:**
  - `age` (integer) - The new age to be set.
- **Response:** `Done!`
- **Example Request Using Postman:**
  - **Method:** POST
  - **URL:** `http://127.0.0.1:5000/sheela`
  - **Body (form-data):**
    - Key: `age`
    - Value: `35`
- **Example Response:** `Done!`

## Testing with Postman

1. **Open Postman.**
2. **To test the POST endpoint:**
   - Set the method to `POST`.
   - Enter the URL `http://127.0.0.1:5000/sheela`.
   - Go to the `Body` tab and select `x-www-form-urlencoded`.
   - Add a key-value pair for `age`.
   - Click `Send`.
   - You should receive a `Done!` response.

3. **To test the GET endpoints:**
   - Set the method to `GET`.
   - Enter the URL for the endpoint you want to test, e.g., `http://127.0.0.1:5000/sit`.
   - Click `Send`.
   - You should receive the appropriate response message.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
