# littlelemon
Description of the project
This is the final project for Back-End Developer Capstone course (Meta Back-End Developer Professional Certificate) to build an API for the Little Lemon restaurant.

Main tasks for the project:

Connect the Little Lemon restaurant back-end to MySQL
Set up a Little Lemon restaurant booking API
Insert booking data in the database via the booking API
API URL
Localhost base URL is http://127.0.0.1:8000


Getting Started
Installation and Database Setup
Clone the repo by running

git clone https://github.com/yonic90/littlelemon

Create the virtual environment for the project directory

python3 -m venv <name>
  
  Activate the virtual environment:

source <name>/bin/activate
  
  Installing Python Dependencies
Once the virtual environment is setup and running, install the required dependencies by navigating to the project directory and running:

pip install -r requirements.txt
This will install all of the required packages in the requirements.txt file.
  
  
Database Setup
The project uses MySQL database.

Change settings (USER and PASSWORD) in littlelemon/settings.py, you should use your credentials.

DATABASES = { "default": { ... "USER" : "admindjango", "PASSWORD" : "employee@123!", ... }

Generate database tables from the models:

python3 manage.py makemigrations
python3 manage.py migrate
  
  Running the Server
Switch to the project directory and ensure that the virtual environment is running.

python3 manage.py runserver
  
Admin credentials:
  admin,
  admin
