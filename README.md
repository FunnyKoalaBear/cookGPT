# 🍽️ CookGPT - Smart Recipe & Pantry Management System

CookGPT is a Django-powered web application that helps users manage their pantry inventory and discover meal recipes based on available ingredients. The application features an intuitive interface for tracking food items across different categories and planning meals efficiently.

## ✨ Features

### 🥗 Pantry Management
- **Categorized Inventory**: Organize ingredients into 6 categories:
  - Vegies & Fruits
  - Proteins
  - Carbs
  - Sauces & Spices
  - Beverages
  - Special Items
- **Quantity Tracking**: Track ingredient quantities with various units (kg, g, ml, l, tsp, tbsp, cups, pieces, slices)
- **Interactive Controls**: Add, edit, and remove pantry items with intuitive +/- buttons
- **Real-time Updates**: Dynamic JavaScript interface for seamless pantry management

### 🍳 Recipe System
- **Custom Recipes**: Create and save personal recipes
- **Ingredient Integration**: Link recipes with pantry ingredients
- **Step-by-Step Instructions**: Detailed cooking instructions with numbered steps
- **User-Specific Collections**: Each user maintains their own recipe collection

### 👤 User Management
- **Authentication System**: Secure user registration and login
- **Personal Accounts**: Individual pantry and recipe management per user
- **Session Management**: Secure user sessions with Django's built-in authentication

### 🎨 Modern UI/UX
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS
- **Clean Layout**: Organized grid-based layout for easy navigation
- **Visual Feedback**: Color-coded buttons and intuitive controls
- **Custom Styling**: Attractive background and modern design elements

## 🛠️ Technology Stack

- **Backend**: Django 5.1.7 (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Database**: SQLite (default Django database)
- **Authentication**: Django's built-in user authentication system

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/FunnyKoalaBear/cookGPT.git
cd cookGPT
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
cookGPT/
├── cookGPT/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── myApp/                   # Main application
│   ├── migrations/          # Database migrations
│   ├── static/myApp/        # Static files (CSS, JS, images)
│   │   ├── cookGPT.css
│   │   ├── cookGPT.js
│   │   ├── pantry.js
│   │   └── background3.jpg
│   ├── templates/myApp/     # HTML templates
│   │   ├── index.html       # Homepage
│   │   ├── pantry.html      # Pantry management
│   │   ├── designMeal.html  # Meal planning
│   │   ├── meals.html       # Recipe viewing
│   │   ├── login.html       # User login
│   │   ├── register.html    # User registration
│   │   └── layout.html      # Base template
│   ├── models.py            # Database models
│   ├── views.py             # Application logic
│   ├── urls.py              # App URL routing
│   └── admin.py             # Django admin configuration
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── README.md                # This file
```

## 🗄️ Database Models

### User Model
- Extends Django's AbstractUser
- Stores user authentication information

### Ingredient Model
- **Fields**: name, category, quantity, unit_of_measurement
- **Categories**: vegies, proteins, carbs, sauces, special, beverage
- **Units**: g, kg, ml, l, tsp, tbsp, cup, piece, slice

### Pantry Model
- Links users to their ingredient collections
- Separate ManyToMany fields for each category
- User-specific pantry management

### MyRecipe Model
- User-specific recipe storage
- Links to ingredient collections
- Recipe name and user association

### InstructionStep Model
- Step-by-step cooking instructions
- Ordered by step number
- Linked to specific recipes

## 🎯 Key Features Explained

### Pantry Management System
The pantry system allows users to:
- Add ingredients with specific quantities and units
- Organize items by food categories
- Update quantities with +/- buttons
- Remove items with trash button
- View all items in an organized grid layout

### Interactive JavaScript
- Real-time form submission without page reload
- Dynamic list updates
- Category-specific ingredient management
- Responsive user interface controls

### User Authentication
- Secure registration and login system
- Session-based authentication
- User-specific data isolation
- Password protection

## 🚀 Usage

1. **Register/Login**: Create an account or log in to access your personal pantry
2. **Manage Pantry**: Add ingredients to different categories with quantities and units
3. **Create Recipes**: Design custom recipes using your pantry ingredients
4. **Plan Meals**: Use the meal planning feature to organize your cooking
5. **Track Inventory**: Monitor ingredient quantities and update as needed

## 🔧 Configuration

### Settings Configuration
Key settings in `cookGPT/settings.py`:
- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Configure for production deployment
- **SECRET_KEY**: Change for production (keep secure)
- **DATABASE**: Currently configured for SQLite

### Static Files
Static files are served from `myApp/static/myApp/`:
- CSS stylesheets
- JavaScript files
- Images and media

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **FunnyKoalaBear** - Initial work - [GitHub Profile](https://github.com/FunnyKoalaBear)

## 🙏 Acknowledgments

- Django framework for the robust backend
- Tailwind CSS for the modern styling
- Python community for excellent documentation and support

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Provide steps to reproduce any bugs

---

**Happy Cooking! 🍳✨**
