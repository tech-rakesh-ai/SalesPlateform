# Sales_Platform

## Project Description

Sales_Platform is a Django-based platform for managing user accounts and product sales. It includes features for user
registration, authentication, and simulating product sales with sample data.

## Features

- **User Management**:
    - Custom user model (`CustomUser`) with extended fields (username, name, age, gender, email, phone, etc.).
    - Address model for storing user addresses.

- **Product Sales**:
    - Model for `Product` with fields for name and price.
    - Model for `Sale` linking users (`CustomUser`) to products (`Product`) with a sale date.

- **Management Commands**:
    - `custom_users.py`: Creates 50 custom user accounts with dummy data fetched from an external
      API (`https://dummyjson.com/users`).
    - `simulate_sales.py`: Simulates 500 product sales by randomly assigning users to products.

## Basic Setup

### Prerequisites

- Python (version 3.8 or higher)
- Django (version 5.0.1)
- PostgreSQL database (update settings.py as per your configuration)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/tech-rakesh-ai/Sales_Platform.git
   cd Sales_Platform
   ```

2. Create a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL database:
    - Create a PostgreSQL database (`sales_platform_db` for example).
    - Update `settings.py` with your PostgreSQL database configuration.

5. Apply migrations and create a superuser:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Load initial data (optional):
    - You can load initial data using Django fixtures or admin interface for Products.

7. Run the development server:

   ```shell
   python manage.py runserver
   ```

### Usage

- Access the Django admin interface at `http://localhost:8000/admin/` to manage users, products, and sales.
- Use the API endpoints or management commands to create users and simulate product sales.

### API Endpoints (if applicable)

- **User Management**: `/accounts/register/`, `/accounts/login/`
- **Product Sales**: Endpoint for fetching and managing product sales.

### Example Management Commands

```bash
python manage.py custom_users  # Creates 50 custom user accounts
python manage.py simulate_sales  # Simulates 500 product sales
```

## Contributors

- Rakesh Kumar (@tech-rakesh-ai)