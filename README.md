## Project Overview

A realistic FastAPI-based blogging platform with user authentication and authorization. Users can sign up, log in, and manage their profiles. Authenticated users can create, edit, and delete their own blog posts, while all users can read posts. Each blog post is linked to its author, providing a secure and user-specific blogging experience.

## Technologies Used

* Python
* FastAPI
* SQLite 
* JWT (JSON Web Tokens) for authentication

## Getting Started

### Prerequisites

* Python 3.6+
* Virtual environment setup

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/APARNA987/fastapi-blog-platform.git
   cd fastapi-blog-platform
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On MacOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   uvicorn Blog.main:app --reload
   ```
## Features & Usage

- Sign up and log in with a unique user account
- Authenticated users can create, update, and delete their own blog posts
- All users (even without login) can read public blog posts
- Users can update their own profile info

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


