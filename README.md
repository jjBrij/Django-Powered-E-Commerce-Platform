# 🛒 Django E-Commerce Platform

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

A full-featured, modern e-commerce platform built with Django and Django REST Framework. This project provides a complete online shopping experience with user authentication, product management, shopping cart, and order processing.

## ✨ Features

- 🔐 **User Authentication & Authorization**
  - User registration and login
  - Password reset functionality
  - User profile management
  
- 🛍️ **Product Management**
  - Browse product catalog
  - Detailed product views
  - Product images and descriptions
  - Category-based organization

- 🛒 **Shopping Cart**
  - Add/remove items
  - Update quantities
  - Persistent cart across sessions

- 📦 **Order Management**
  - Order placement
  - Order history
  - Order tracking

- 👤 **User Profiles**
  - Personal information management
  - Address management
  - Order history view

- 🎨 **Responsive Design**
  - Mobile-friendly interface
  - Clean and intuitive UI

## 🚀 Tech Stack

**Backend:**
- Python 3.11
- Django 4.x
- Django REST Framework
- SQLite (Development) / PostgreSQL (Production Ready)

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Bootstrap (if applicable)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- pip (Python package manager)
- Git
- Virtual environment tool (venv)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jjBrij/Django-Powered-E-Commerce-Platform.git
cd Django-Powered-E-Commerce-Platform
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (for production)
# DB_NAME=your_db_name
# DB_USER=your_db_user
# DB_PASSWORD=your_db_password
# DB_HOST=localhost
# DB_PORT=5432
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 7. Load Sample Data (Optional)

```bash
python manage.py loaddata fixtures/sample_data.json
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
Django-Powered-E-Commerce-Platform/
│
├── ec/                          # Main project directory
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── app/                         # Main application
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   └── app/
│   │       ├── index.html
│   │       ├── productdetail.html
│   │       ├── profile.html
│   │       ├── password_reset_*.html
│   │       └── ...
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL configuration
│   ├── forms.py                # Form definitions
│   ├── admin.py                # Admin configuration
│   └── tests.py                # Test cases
│
├── media/                       # User-uploaded files
│   └── product/                # Product images
│
├── static/                      # Static files (CSS, JS, Images)
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## 🎯 Usage

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`
- Add/Edit/Delete products
- Manage users
- View and manage orders
- Configure site settings

### User Features

1. **Browse Products**: Navigate through the product catalog
2. **Product Details**: Click on any product for detailed information
3. **Add to Cart**: Add products to your shopping cart
4. **Checkout**: Complete your purchase
5. **Profile**: Manage your profile and view order history

## 🔌 API Endpoints (If REST API is implemented)

```
GET    /api/products/          # List all products
GET    /api/products/<id>/     # Get product details
POST   /api/cart/add/          # Add item to cart
GET    /api/cart/              # View cart
POST   /api/orders/            # Create order
GET    /api/orders/<id>/       # Get order details
```

## 🧪 Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 🚢 Deployment

### Preparing for Production

1. **Update Settings:**
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use PostgreSQL or MySQL instead of SQLite
   - Set up proper `SECRET_KEY`

2. **Collect Static Files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Security Checklist:**
   ```bash
   python manage.py check --deploy
   ```

### Deployment Options

- **Heroku**: Use the Heroku CLI and Procfile
- **AWS**: Deploy using Elastic Beanstalk or EC2
- **DigitalOcean**: Use App Platform or Droplets
- **PythonAnywhere**: Simple deployment for Django apps

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📝 Code Style

- Follow PEP 8 guidelines
- Write meaningful commit messages
- Add docstrings to functions and classes
- Include comments for complex logic

## 🐛 Known Issues

- List any known bugs or limitations here

## 📅 Future Enhancements

- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Email notifications
- [ ] Advanced search and filtering
- [ ] Product recommendations
- [ ] Multi-vendor support
- [ ] Mobile app (React Native/Flutter)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**B Mohan Prasad**
- GitHub: [@jjBrij](https://github.com/jjBrij)

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- Bootstrap (if used)
- All contributors and supporters

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Contact: [Your Email]

---

<div align="center">
  <p>Made with ❤️ using Django</p>
  <p>⭐ Star this repo if you find it helpful!</p>
</div>
