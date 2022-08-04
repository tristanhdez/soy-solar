## Getting Started

First of all, thank you so much to take us in consideration to colaborate with Solar. The intention of Solar is encourange the students to contribute and get/improve your skills to get some experience. <br>
In the future you'll thanks us, Solar and we will too.

If you want to help but don't know where to start, here are some low-risk/isolated tasks:
<br>
https://github.com/tristanhdez/soy-solar/issues


### Prerequisites

Things you need before:

* Python 3.x
* Flask
* Pip

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
SECRET_KEY="YOUR_SUPER_SECRET_KEY"
```

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
