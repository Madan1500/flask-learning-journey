# Flask Learning Journey 🚀

This repository documents my learning journey with Flask web framework. Each commit represents a new concept learned and implemented.

## About This Project

This is a Flask learning project following along with YouTube tutorials and documentation. The goal is to understand Flask fundamentals through hands-on coding practice.

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Madan1500/flask-learning-journey.git
cd flask-learning-journey
```

### 2. Create a virtual environment
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## Current Features

- **Hello World Route** (`/`) - Basic Flask route returning HTML
- **Simple Hello Route** (`/hello`) - Alternative hello endpoint returning plain text
- **Dynamic Greet Route** (`/greet/<name>`) - Personalized greeting using URL parameters

## Learning Progress

### ✅ Completed
- [x] Setting up Flask project structure
- [x] Creating virtual environment
- [x] Basic Flask app with Hello World route
- [x] Understanding Flask routing basics
- [x] Dynamic routes with URL parameters
- [x] Multiple route endpoints

### 🔄 In Progress
- [ ] HTTP methods (GET, POST, etc.)
- [ ] Templates with Jinja2
- [ ] Forms handling
- [ ] Database integration

## Useful Commands

### Generate requirements.txt
```bash
pip freeze > requirements.txt
```

### Install from requirements.txt
```bash
pip install -r requirements.txt
```

## Learning Reflections 📝

### Dynamic URL Parameters
**What I learned:**
- How to capture URL segments using `<variable_name>` syntax
- The captured value is automatically passed as a parameter to the route function
- URL parameters are always strings by default
- Flask supports type converters like `<int:id>` or `<float:price>`

**Example Usage:**
```python
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"
```

**Testing:**
- Visit `http://localhost:5000/greet/Madan` → Returns "Hello, Madan!"
- Visit `http://localhost:5000/greet/Flask` → Returns "Hello, Flask!"

**Challenges faced:**
- Initially confused about the syntax `<name>` vs `{name}`
- Learned that the parameter name in the URL must match the function parameter
- Understanding that URL parameters create dynamic routes

**Key takeaways:**
- Dynamic routes make web applications more flexible and user-friendly
- URL parameters are a fundamental concept for building REST APIs
- This opens the door to more complex routing patterns

## Learning Resources

- Flask Official Documentation
- YouTube tutorials
- Flask Mega-Tutorial

---
**Note**: This is a learning project - code may not follow production best practices as it focuses on understanding core concepts.

