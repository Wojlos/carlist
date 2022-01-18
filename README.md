# Wojlos carlist app

App on heroku `carlist-api.herokuapp.com/api/cars/`
## Setup

Clone the repository:

```sh
$ git clone https://github.com/Wojlos/carlist.git
$ cd carlist
```

Install python venv package:
```sh
$pip install venv
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ python -m venv env
$ source env/bin/activate
```

Install required python packages:
```sh
$ pip install -r requirements.txt
```

Make migrations and migrate :
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Run unit tests:
```sh
$ python manage.py test
```

Run python development server:
```sh
$ python manage.py runserver
```

## Walkthrough

Navigate to `http://127.0.0.1:8000/`
Use this endpoints and their functionalities

### LIST/ POST car instances
```sh
api/cars/
```

### RETRIVE/DELETE car instance

```sh
api/cars/{id}
```

### RATE car instance

```sh
api/rate/
```

### LIST car instances ordered by number of reviews

```sh
api/popular/
```
