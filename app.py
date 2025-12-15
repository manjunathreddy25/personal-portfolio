from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-this-in-prod' # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manjunath.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Models ---
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(200), nullable=False) # Technologies list
    description = db.Column(db.Text, nullable=False) # Full bullet points
    image_url = db.Column(db.String(200))
    link = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Helpers ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Initial Data Seeder ---
def seed_data():
    if not Project.query.first():
        # Project 1: Face Recognition System
        summ1 = "Technologies: Python, OpenCV, Image Processing"
        desc1 = """• Built a real‑time face recognition system for user authentication using Python and OpenCV.
• Implemented image detection, encoding, and verification logic with modular Python code.
• Improved recognition accuracy through preprocessing techniques such as grayscale conversion and face alignment.
• Gained practical experience in algorithms, debugging, and performance optimization."""
        p1 = Project(title="Face Recognition System (Academic Project)", summary=summ1, description=desc1, image_url="https://via.placeholder.com/300/0ea5e9/ffffff?text=Face+Recognition", link="#")
        
        # Project 2: Personal Portfolio Website
        summ2 = "Technologies: HTML, CSS, JavaScript, Python (Flask), Git"
        desc2 = """• Designed and developed a responsive personal portfolio website showcasing skills and projects.
• Created backend routes using Flask to handle contact form submissions.
• Applied basic REST principles and integrated frontend with backend logic.
• Used GitHub for version control and project management."""
        p2 = Project(title="Personal Portfolio Website (Personal Project)", summary=summ2, description=desc2, image_url="https://via.placeholder.com/300/0ea5e9/ffffff?text=Portfolio", link="#")
        
        # Project 3: AWS Cloud Deployment
        summ3 = "Technologies: Python, AWS EC2, RDS, NGINX, Git"
        desc3 = """• Deployed a Python‑based web application on AWS using EC2 and RDS.
• Configured NGINX for application hosting and improved reliability.
• Learned deployment workflows, environment setup, and database connectivity.
• Strengthened understanding of how backend applications run in real‑world environments."""
        p3 = Project(title="AWS Cloud Deployment Project", summary=summ3, description=desc3, image_url="https://via.placeholder.com/300/0ea5e9/ffffff?text=AWS+Cloud", link="#")
        
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.commit()
    
    if not BlogPost.query.first():
        b1 = BlogPost(title="Journey as a Python Developer", content="As a Computer Science graduate, I started my journey with Python...")
        db.session.add(b1)
        db.session.commit()

# --- Routes ---
@app.route('/')
def home():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('home.html', projects=projects, title="Home")

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project, title=project.title)

@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog.html', posts=posts, title="Blog")

@app.route('/blog/<int:post_id>')
def post_detail(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post, title=post.title)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    new_message = ContactMessage(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message')
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'success': 'Message sent!'})

# --- Admin Routes ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple hardcoded check for demonstration (fresher level)
        if username == 'admin' and password == 'admin':
            session['user_id'] = 1
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials')
    return render_template('login.html', title="Login")

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('admin.html', projects=projects, posts=posts, messages=messages, title="Admin")

@app.route('/admin/add_post', methods=['POST'])
@login_required
def add_post():
    title = request.form['title']
    content = request.form['content']
    new_post = BlogPost(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    flash('Post created!')
    return redirect(url_for('admin'))

@app.route('/admin/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted!')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True)
