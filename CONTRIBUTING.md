## Getting Started

First of all, thank you so much to take us in consideration to colaborate with Solar. The intention of Solar is encourange the students to contribute and get/improve your skills to get some experience. <br>
In the future you'll thanks us, Solar and we will too.

If you want to help but don't know where to start, here are some low-risk/isolated tasks:
<br>
https://github.com/tristanhdez/soy-solar/issues


### Prerequisites

Things you need before:
```
* Python 3.x
* MySQL
* Flask
```
### Installation

This is the easier way to start with our project:

```
$ pip install -r requirements.txt
$ export FLASK_DEBUG=development
```

## Database Configuration

Please, take in consideration the next arguments on `Config.py`:

```
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'username'
    MYSQL_DATABASE_PASSWORD = '*******'
    MYSQL_DATABASE_DB= 'database_name'
```

Remember create your `.env`:
```
SECRET_KEY = 'YOUR_SUPER_SECRET_KEY'
```

## Important

Run your project on `http://127.0.0.1:5000/`

## Project Layout


    ├─ .github/             Templates and Dependabot yml
    ├─ apps/                Apps of Solar
        ├─ guest/           Guest Section
        ├─ home/            Home Section
        ├─ student/         Student Section
        ├─ utils/           Classes
    ├─ db/                  Solar Template Database
    ├─ docs/                Documentation
    ├─ static/              Design/Styles
        ├─ css/             CSS Styles
            ├─ error/       Error Styles
                ├─ client/  Client Styles
                ├─ server/  Server Styles
            ├─ guest/       Guest Styles
            ├─ home/        Home Styles
            ├─ student/     Student Styles
        ├─ img/             Images of Solar
            ├─ home/        Home Page Images
                ├─ index/   Index Images
                ├─ section/ Section Images
            ├─ icons/       Icons of Solar
            ├─ wallpaper/   Wallpapers of Solar
        ├─ js/              Scripts Functions to return answers of questions
            ├─ guest/       Guest Scripts
            ├─ student/     Student Scripts
    ├─ templates/           HTML Documents
        ├─ errors/          Errors templates
            ├─ client/      Client Templates
            ├─ server/      Server Templates
        ├─ guest/           Guest Templates
        ├─ home/            Home templates
        ├─ student/         Student Templates
    ├─ test/                Testing
        ├─ pytest/          Testing with PyTest


### Credentials

Take in consideration the next data by default on database template `soy-solar-template` :

Student:

```
Name: Tristán Pérez Pérez
Code: 000000000
Career: INGC
Email: tristan@gmail.com
Tutor: Juan Perez
```

Tutor:

```
Name: Juan Pérez El Tutor
Email: Juanito69@gmail.com
Career: INGC
```

You can use Fake data and insert in the Database, for example you can use [Faker](https://github.com/joke2k/faker) to start to work.
