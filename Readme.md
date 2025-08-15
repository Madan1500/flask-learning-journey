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

## 🌿 Git Workflow & Branching Strategy

This repository follows a **three-branch workflow** for professional development practices:

```
main (initial work) → dev (development) → prod (production)
```

### Branch Purposes

- **`main`** - Initial development and learning commits
- **`dev`** - Active development, new features, experiments  
- **`prod`** - Stable, production-ready code for deployment

### Workflow Process

1. **Learning & Initial Development**: Work directly on `main`
2. **Feature Development**: 
   ```bash
   git checkout main
   git pull origin main
   # Make your changes
   git add .
   git commit -m "feat: add new learning concept"
   git push origin main
   ```
3. **Merge to Development**:
   ```bash
   git checkout dev
   git merge main
   git push origin dev
   ```
4. **Deploy to Production**:
   ```bash
   git checkout prod  
   git merge dev
   git push origin prod
   ```

### Quick Commands

```bash
# Check current branch
git branch

# Switch branches
git checkout main
git checkout dev
git checkout prod

# View all branches
git branch -a
```

## 🌐 Live Deployment

**🚀 LIVE SITE**: https://flask-learning-journey.onrender.com  
**📁 Repository**: https://github.com/Madan1500/flask-learning-journey

### Live Routes (Test Them!):
- **Home**: https://flask-learning-journey.onrender.com/
- **Hello**: https://flask-learning-journey.onrender.com/hello  
- **Greet**: https://flask-learning-journey.onrender.com/greet/YourName

**Deployment Status**: ✅ Successfully deployed from `prod` branch

### Deploy to Render (Recommended)

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New" → "Web Service"
3. Connect your GitHub account and select this repository (`flask-learning-journey`)
4. **Important**: Change the branch from `main` to `prod` in deployment settings
5. Render will automatically detect the `render.yaml` configuration
6. Click "Deploy" - your app will be live in a few minutes!

**Note**: Always deploy from the `prod` branch for stable releases.

### Alternative: Deploy to Railway

1. Go to [Railway.app](https://railway.app) and login with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select `flask-learning-journey` repository
4. Railway will auto-deploy using the existing configuration

### Alternative: Deploy to Heroku

```bash
# Install Heroku CLI first
heroku create your-flask-app-name
git push heroku main
```

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
- [x] Professional Git workflow (main → dev → prod)
- [x] Production deployment with Render
- [x] Live website hosting

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

