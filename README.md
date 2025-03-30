
Submitted By: Kushagra 

Objective-
The goal is to create a fully functional blog system using Django and integrate an external API (https://restcountries.com/) to fetch country-related data.

Features-
List Blogs: Display a list of all blogs with titles and descriptions.

Blog Details: View detailed information about a selected blog post.

API Integration: Fetch and display country details using https://restcountries.com/.

Technology Stack-

Backend: Django, Django REST Framework

Database: SQLite (default for Django)

API: REST API from https://restcountries.com/

Version Control: Git and GitHub

Project Setup Instructions-

1. Clone the Repository

$ git clone https://github.com/kushagrasingh01/Blog_System.git
$ cd Blog_System

2. Create a Virtual Environment

$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

$ pip install -r requirements.txt

4. Apply Migrations

$ python manage.py migrate

5. Create a Superuser (For Admin Access)

$ python manage.py createsuperuser

Follow the prompts to enter a username, email, and password.

6. Run the Development Server

$ python manage.py runserver

Access the application at: http://127.0.0.1:8000

API Integration

The project integrates https://restcountries.com/ to fetch country-related details.

Country information is displayed in the blog details section.

How to Use the Application-

Open the web browser and go to http://127.0.0.1:8000

View the list of available blogs.

Click on a blog to view its details.

Search for a blog using the search bar.

Like or comment on a blog post (if logged in).

Admin users can add, edit, or delete blog posts.
