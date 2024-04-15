Learning Lab Web Project
This project is a Flask web application designed to manage student records. It consists of a web application container and a MySQL database container, both orchestrated using Docker Compose.

Project Structure
csharp
Copy code
learning_lab_web/
├── db/
│   └── init.sql
├── docker-compose_flask.yml
└── flask_project/
    ├── app.py
    ├── Dockerfile
    ├── requirements.txt
    ├── static/
    │   ├── abd4.png
    │   ├── alnafi.jpg
    │   └── style.css
    └── templates/
        ├── course.html
        ├── data.html
        ├── demo.html
        ├── index.html
        ├── JIRA_TICKET_CREATION.html
        ├── login_page.html
        ├── sample.html
        └── table.html
How to Run
Ensure Docker is installed on your system.
Navigate to the project directory.
Run the following command:
Copy code
docker-compose -f docker-compose_flask.yml up
This will start the Flask web application and MySQL database containers.

Accessing the Application
The web application is accessible at http://localhost:9000.
The MySQL database is accessible at port 3400.
Features
User Authentication: Users can log in with their username and password.
Student Record Management: Trainers can create and view student records.
JIRA Integration: Integration with JIRA for creating tickets.
Technologies Used
Flask
MySQL
Docker
HTML/CSS
JIRA Python Library
Author
[Muhammad Abdullah]

License
This project is licensed under the MIT License.

