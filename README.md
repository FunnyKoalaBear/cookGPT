# 🍽️ CookGPT - Smart Recipe & Pantry Management System

CookGPT is a full-stack Django web application designed to help users efficiently manage their kitchen pantry and discover recipes tailored to the ingredients they already have. Unlike simple recipe websites, CookGPT combines inventory tracking, custom recipe management, and AI-powered meal planning into one cohesive platform. Users can register for accounts, maintain their own personalized pantries, create recipes, and receive intelligent recipe suggestions from OpenAI’s GPT model.

The application provides a responsive and modern interface built with Tailwind CSS, ensuring usability across devices. Pantry items are categorized for clarity, quantities are tracked with multiple measurement units, and interactive JavaScript updates make managing the pantry seamless. On the recipe side, users can write their own recipes or rely on CookGPT’s AI integration to generate creative meal ideas and cooking instructions. The platform therefore bridges the gap between pantry management and meal planning, transforming the way users organize their food and cook.

## Distinctiveness and Complexity

CookGPT satisfies the distinctiveness requirement because it is fundamentally different from the course’s existing projects. While Project 2 (Commerce) is focused on buying and selling items in a marketplace, and Project 4 (Network) emphasizes social interactions between users, CookGPT does neither. It is not an e-commerce platform, nor is it a social network. Instead, it is a pantry and recipe management system enhanced by AI-powered recommendations, a use case not covered in any prior project. The core concept revolves around optimizing a user’s cooking experience by connecting their available ingredients with intelligent meal planning, which clearly distinguishes it from other course assignments.

The project also achieves complexity well beyond earlier projects. At its foundation, CookGPT defines several interrelated database models — users, ingredients, pantries, recipes, and step-by-step instructions — and connects them through relationships such as ManyToMany fields. Each user maintains an isolated pantry and recipe collection, which requires careful authentication and session handling. On the frontend, the pantry interface incorporates dynamic JavaScript controls that allow items to be added, edited, and removed without refreshing the page, ensuring a smooth and interactive experience. This combination of real-time updates with Django’s backend goes beyond the simpler CRUD implementations of previous projects.

Complexity is further increased through the integration of external AI services. By connecting to the OpenAI API, the application can generate recipes, suggest substitutions, provide nutritional insights, and even assist with weekly meal planning. This layer of AI-powered functionality requires handling API calls securely, parsing and formatting the responses, and seamlessly integrating them into the user’s workflow. Such an integration adds significant technical depth compared to prior projects that rely only on Django’s built-in capabilities.

In addition, the application’s responsive design with Tailwind CSS ensures that it functions smoothly on both desktop and mobile devices, which introduces challenges in layout and usability that were not present in earlier projects. The system also requires proper handling of environment variables (for API keys and secret settings), which reflects real-world deployment concerns.

Altogether, the project demonstrates both distinctiveness — by targeting a problem domain not addressed in CS50W’s set projects — and complexity — by combining advanced Django features, dynamic JavaScript interactivity, and external AI integration into a single cohesive application. CookGPT is therefore a meaningful step beyond the earlier assignments, both in scope and technical implementation.

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
- **AI-Powered Suggestions**: Get recipe recommendations using OpenAI GPT based on your pantry ingredients
- **Ingredient Integration**: Link recipes with pantry ingredients
- **Step-by-Step Instructions**: Detailed cooking instructions with numbered steps
- **User-Specific Collections**: Each user maintains their own recipe collection
- **Smart Meal Planning**: AI-assisted meal planning based on available ingredients

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
- **AI Integration**: OpenAI GPT API for recipe suggestions and meal planning
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Database**: SQLite (default Django database)
- **Authentication**: Django's built-in user authentication system

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)
- OpenAI API key (for AI-powered features)

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
pip install django openai
```

### 4. Set Up OpenAI API Key
Create a `.env` file in your project root and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-openai-api-key-here
```

Or set it as an environment variable:
```bash
# Windows
set OPENAI_API_KEY=your-openai-api-key-here

# macOS/Linux
export OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
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
├── api.py                   # OpenAI API integration
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── .env                     # Environment variables (create this)
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

### AI-Powered Recipe Suggestions
- **Smart Recommendations**: Generate recipe suggestions based on available pantry ingredients
- **Ingredient Optimization**: AI analyzes your pantry to suggest recipes that use the most ingredients
- **Dietary Preferences**: Customize suggestions based on dietary restrictions and preferences
- **Nutritional Information**: Get nutritional insights for suggested recipes
- **Cooking Tips**: AI-generated cooking tips and techniques for better results

## 🚀 Usage

1. **Register/Login**: Create an account or log in to access your personal pantry
2. **Manage Pantry**: Add ingredients to different categories with quantities and units
3. **Get AI Suggestions**: Use the AI-powered feature to get recipe recommendations based on your pantry
4. **Create Recipes**: Design custom recipes using your pantry ingredients
5. **Plan Meals**: Use the meal planning feature to organize your cooking
6. **Track Inventory**: Monitor ingredient quantities and update as needed

## 🔧 Configuration

### Settings Configuration
Key settings in `cookGPT/settings.py`:
- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Configure for production deployment
- **SECRET_KEY**: Change for production (keep secure)
- **DATABASE**: Currently configured for SQLite
- **OPENAI_API_KEY**: Set your OpenAI API key for AI features

### Environment Variables
For security, use environment variables for sensitive data:
```python
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', 'your-fallback-secret-key')
```

### Static Files
Static files are served from `myApp/static/myApp/`:
- CSS stylesheets
- JavaScript files
- Images and media

## 🤖 AI Integration

### OpenAI Features
The application integrates with OpenAI's GPT API to provide:

- **Recipe Generation**: Create recipes based on available ingredients
- **Meal Planning**: Smart meal suggestions for the week
- **Ingredient Substitutions**: Alternative ingredients when items are missing
- **Cooking Instructions**: Detailed step-by-step cooking guidance
- **Nutritional Analysis**: Health insights for meals and ingredients

### API Usage Example
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_recipe(ingredients):
    prompt = f"Create a recipe using these ingredients: {', '.join(ingredients)}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful cooking assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content
```

### Getting an OpenAI API Key
1. Visit [OpenAI's website](https://platform.openai.com/api-keys)
2. Create an account or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and securely store your API key

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
