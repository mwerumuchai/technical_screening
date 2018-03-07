# Technical Screening

#### Created by [Esther Muchai](https://github.com/mwerumuchai) 

## Setup/Installation Requirements

### Prerequisites
* Python3.6.3
* Virtual Environment
* Postgres Database
* Internet

### Installation Process
1. Copy/Download repository link
2. Run git clone `[<repository-url>]`(https://github.com/mwerumuchai/technical_screening.git) in your terminal
3. Write `cd technical_screening`
4. Create a virtual environment by `python3.6 -m venv virtual`
5. create a .env file `touch .env` then add 
    `*SECRET-KEY=<your secret key>` 
    `*DEBUG=TRUE`
6. Activate your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` Or you can use `pip3 install -r requirements.txt`
8. Create Postgres Database
    `*psql`
    `*CREATE DATABASE movie`
    
 9. In settings.py, change the database information
    `*DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'movies',
            'USER': '<postgres_username>',
            'PASSWORD':'<postgres_password>',
          }
      }`
 10. Run `./manage.py runserver` 
          *Running on http://127.0.0.1:8000/admin 

### Technologies Used
* Python3.6.3
* Django 2.0
* Postgres Database

### License

MIT (c) 2018 [Esther Muchai](https://github.com/mwerumuchai) 
