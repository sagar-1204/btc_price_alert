# BTC Price Alert

A Flask-based application to set and manage price alerts for Bitcoin (BTC) and other cryptocurrencies. Users can set a target price for a specific cryptocurrency, and the application will notify them via email when the target price is reached.

## Description

This application allows users to:
- Create alerts for different cryptocurrencies at target prices.
- Receive email notifications when the target prices are achieved.
- Manage (view, update, delete) their alerts.

## Getting Started

### Dependencies

- Python 3.6+
- Flask
- PostgreSQL
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Requests
- Other dependencies are listed in the `requirements.txt` file.

### Setting Up and Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/sagar-1204/btc_price_alert.git
Navigate to the project directory:

cd btc_price_alert
Install the required packages:

pip install -r requirements.txt
Configuring the Application
Set up a PostgreSQL database and update the SQLALCHEMY_DATABASE_URI in app.py with your database credentials.
Set your JWT secret key in the application configuration.
Executing the Program
Run the Flask application:


python app.py
API Endpoints
User Registration
URL: /auth/register
Method: POST
Data Params:
json
Copy code
{
    "username": "user",
    "email": "user@example.com",
    "password": "your_password"
}
User Login
URL: /auth/login
Method: POST
Data Params:
json
Copy code
{
    "email": "user@example.com",
    "password": "your_password"
}
Create Alert
URL: /alerts/create/
Method: POST
Data Params:
json
Copy code
{
    "email": "user@example.com",
    "crypto": "BTC",
    "target_price": 30000
}
Delete Alert
URL: /alerts/delete/<alert_id>/
Method: DELETE
View Alerts
URL: /alerts/
Method: GET
