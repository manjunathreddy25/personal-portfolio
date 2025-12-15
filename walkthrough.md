# Manjunath - Project Walkthrough

## Overview
This is a Personal Portfolio & Blog application built with Flask. features a modern Sky Blue monochrome design.

## How to Run
1.  **Open Terminal** in the project directory: `c:\Users\Manjunath\OneDrive\DA PROJECTS\Python_project`
2.  **Run the application**:
    ```bash
    python app.py
    ```
3.  **Open in Browser**: Go to `http://127.0.0.1:5000/`

## Features & Verification
### 1. Public Portfolio
-   **Link**: [Home](http://127.0.0.1:5000/)
-   **Verify**: 
    -   Check "About Me", "Skills", "Projects" sections.
    -   Scroll down to see the fade-in animations.
    -   Test the **Contact Form** at the bottom (Use network tab to see API request).

### 2. Blog
-   **Link**: [Blog](http://127.0.0.1:5000/blog)
-   **Verify**:
    -   Click "Blog" in the nav.
    -   You should see sample posts.
    -   Click "Read More" to see the full post.

### 3. Admin Dashboard
-   **Link**: [Admin Login](http://127.0.0.1:5000/login)
-   **Credentials**:
    -   Username: `admin`
    -   Password: `admin`
-   **Verify**:
    -   Login to access the dashboard.
    -   **Add Post**: Try adding a new blog post. Check if it appears on the public Blog page.
    -   **Messages**: Check if contact form messages appear here.
    -   **Delete Post**: Try deleting a post.

## Code Structure
-   `app.py`: Main backend logic (Routes, Models).
-   `templates/`: HTML files (`home.html`, `blog.html`, `admin.html`, etc.).
-   `static/`: CSS and JS files.
-   `manjunath.db`: SQLite database (auto-created on first run).
