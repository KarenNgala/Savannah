# Customer & Orders API

## Overview
This API provides functionality for managing customers and orders.

### Features
- Customer creation and management.
- Order management with SMS notifications.
- OIDC authentication with Google.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KarenNgala/Savannah.git
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
3. Set up environment variables (.env file)
4. Run the migrations:
    ```bash
    python manage.py migrate
5. Start the development server:
    ```bash
    python manage.py runserver
6. API Documentation
You can explore the API documentation at:
- Swagger: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

7. Authentication
- The API uses OIDC authentication with Google. Ensure you log in to obtain an access token, which should be included in requests as follows:

    ```bash
    Authorization: Bearer <token>
8. Running Tests
    ``` bash
    pytest --cov=application tests/  
9. Deployment

Deployment instructions for Azure, including CI/CD setup, are in the deploy/ directory.