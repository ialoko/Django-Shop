# Django-Shop
 
This is a Django-based e-commerce web application designed to help businesses sell products online. The application provides an intuitive interface for managing products, orders, and customers.

## Features
* User authentication and authorization.
* Product catalog management.
* Shopping cart functionality.
* Order management and processing.
* Customer management and order history.
* Payment integration with Paypal.
* Installation

## Installation
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/ialoko/Django-Shop.git
```

Change into the project directory:

```bash
cd myshop
```

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages:

```bash
pip install -r requirements.txt
```

Migrate the database:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Usage
After starting the development server, you can access the application by navigating to http://localhost:8000/ in your web browser. From there, you can login as the superuser you created earlier and begin managing products, orders, and customers.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.



## License

[MIT](https://choosealicense.com/licenses/mit/)





