# Online Shop

This project is an **Online Shop** developed using **Django** as the backend framework and **HTML**, **CSS**, and **JavaScript** for the frontend. The system allows users to browse, buy products, and manage their profiles.

## Features

- **Homepage**: Displays featured products and categories.
- **Product Search**: Allows users to search and filter products.
- **Shopping Cart**: Add products to the cart and manage the cart.
- **User Profiles**: User registration, login, and profile management.
- **Online Payment**: Integration with payment gateways for checkout.
- **Admin Panel**: Admin panel for managing products, orders, and users.

## Technologies Used

This project uses the following technologies:
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (for development) or PostgreSQL (for production)
- **Version Control**: Git

## Prerequisites

Make sure you have the following installed before getting started:

- Python 3.x
- pip (for installing dependencies)
- Git

## Installation and Setup

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/sajjadkargar6131/online_shop.git
cd online_shop
```

### 2. Set up a virtual environment

Create and activate a virtual environment for Python dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

Install the required dependencies with pip:

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Run database migrations to set up the required tables:

```bash
python manage.py migrate
```

### 5. Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

Now, you can view the project by navigating to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Usage

- **User Registration**: To use the online shop, you must first create an account.
- **Browse Products**: You can browse products from the homepage and view detailed information about each product.
- **Add to Cart**: Add products to your shopping cart and proceed to checkout.
- **Payment**: After completing the cart, proceed to the payment process.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Any suggestions or bug reports are also welcome!

## Author

This project is developed by [Sajjad Kargar](https://github.com/sajjadkargar6131).

## License

This project is licensed under the [MIT License](LICENSE).
