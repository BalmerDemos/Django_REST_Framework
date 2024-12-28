# Django_REST_Framework

### Description
**CRUD Operations in Django REST Framework**
This repository contains the CRUD (Create, Read, Update, Delete) functionality for managing items using Django REST Framework (DRF).
This app is part of the larger learning_drf project, which demonstrates how to build RESTful APIs in Django.

---

### Table of Contents
1.  [Installation](#installation)
2.  [Usage](#usage)
3.  [Features](#Features)
4.  [Endpoints](#Endpoints)
5.  [Available Endpoints](#AvailableEndpoints)
6.  [Folder Structure](#FolderStructure)
7.  [SQLiteDatabase](#SQLiteDatabase)
8.  [License](#License)
9.  [Contributing](#contributing)
10. [Disclaimer](#disclaimer)

--- License

### Installation

1. Clone the repository:
    ```bash
   https://github.com/BalmerDemos/Django_REST_Framework

    ```

2. Install the required dependencies: YOU NEED TO HAVE PYTHON PRE-INSTALLED.
    ```bash
    pip install -r requirements.txt
    ```

   **Current Dependencies**:
   - `asgiref==3.8.1`
   - `asgiref==3.8.1`
   - `Django==5.1.4`
   - `djangorestframework==3.15.2`
   - `drf-yasg==1.21.8`
   - `inflection==0.5.1`
   - `packaging==24.2`
   - `pytz==2024.2`
   - `PyYAML==6.0.2`
   - `sqlparse==0.5.3`
   - `typing_extensions==4.12.2`
   - `tzdata==2024.2`
   - `uritemplate==4.1.1`
---

### Usage

1. **Use the crud app**: .
Clone the respository..
Now that you’ve set everything up, you can test the CRUD operations using an API tool like Postman, Insomnia, or directly in the browser.

# To create a table:

- python manage.py makemigrations
- python manage.py migrate

# To run the application:
- python manage.py runserver <port_number>

- http://127.0.0.1:5000/api/items/

2. **GET**:
GET: /api/items/ — Retrieves all items.

3. **POST**:
POST: /api/items/ — Creates a new item.

# add three items, fruits, using POST
- Apple
  Description: A sweet, crisp fruit that comes in various colors like red, green, and yellow. Apples are rich in fiber and vitamins, making them a popular choice for snacks and desserts.

- Banana
  Description: A soft, tropical fruit with a creamy texture, wrapped in a yellow peel. Bananas are an excellent source of potassium and natural energy.

- Orange
  Description: A juicy, citrus fruit known for its bright orange color and tangy flavor. Oranges are rich in vitamin C and are commonly consumed fresh or as juice.

4. **PUT**:
PUT: /api/items/{id}/ — Updates an existing item.
- http://127.0.0.1:5000/api/items/4/


5. **DELETE**:
DELETE: /api/items/{id}/ — Deletes an existing item.
- http://127.0.0.1:5000/api/items/4/


# Features

- Create: Add new items to the database.

- Read: Retrieve a list of items or individual item details.

- Update: Modify existing items.

- Delete: Remove items from the database.

# Endpoints

- Base URL

http://127.0.0.1:5000/api/


# Available Endpoints

Get all items:

- GET /items/

Retrieves a list of all items.

Get a specific item:

- GET /items/<int:pk>/

Retrieves the details of a specific item by ID.

Create a new item:

- POST /items/

Adds a new item to the database.

Update an existing item:

- PUT /items/<int:pk>/

Updates the details of an existing item.

Delete an item:

- DELETE /items/<int:pk>/

Removes an item from the database.

# Folder Structure
crud_app/
-    migrations/   # Database migration files
-    __init__.py
-    admin.py      # Admin interface configuration
-    apps.py       # App configuration
-    models.py     # Database models
-    serializers.py # DRF serializers
-    urls.py       # URL configuration
-    views.py      # API views

# SQLite Database
Check the database directly to verify the changes using python manage.py dbshell.

# License

MIT License

Copyright (c) 2024 [Developed by Balmer Valencia]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

[Include any conditions you want to impose, or leave this section out for a more permissive license.]

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Contributing
Feel free to clone the repository for your own enhancements or bug fixes! Cloning allows you to create a local copy of the project, where you can experiment and make changes without affecting the original repository. If you're unsure how to clone a repository, you can follow a simple guide on the process

# Disclaimer
Please note that this project is for educational purposes only. Any use of the code or information provided is at your own risk.
--------------------------------------------------------------------------------------------------------------
Hey everyone! To all my amazing peers in the second year at Universidad Autónoma De Occidente, I’m excited to share this project with you! I hope you find it super useful and that it sparks some inspiration for your own work. Let’s learn and grow together!

If you have any questions or need assistance, feel free to reach out. Happy coding!

