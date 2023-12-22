<a href="https://softserve.academy/"><img src="https://s.057.ua/section/newsInternalIcon/upload/images/news/icon/000/050/792/vnutr_5ce4f980ef15f.jpg" title="SoftServe IT Academy" alt="SoftServe IT Academy"></a>

***INSERT GRAPHIC HERE (include hyperlink in image)***

# Repository Title Goes Here

> This project aims to facilitate the collaboration between startups and investors, providing a platform for them to discover and connect with each other. It serves as a business-to-business solution, enabling the exchange of information between startups and potential investors.

>  Business-to-business solution B2B

> Django backend serves, Custom Administrative Panel

**Badges will go here**

- build status
- coverage
- issues (waffle.io maybe)
- devDependencies
- npm package
- slack
- downloads
- gitter chat
- license
- etc.

[![Build Status](https://img.shields.io/travis/ita-social-projects/Forum-Sandbox/master?style=flat-square)](https://travis-ci.org/github/ita-social-projects/Forum-Sandbox)
[![Coverage Status](https://img.shields.io/gitlab/coverage/ita-social-projects/Forum-Sandbox/master?style=flat-square)](https://coveralls.io)
[![Github Issues](https://img.shields.io/github/issues/ita-social-projects/Forum-Sandbox?style=flat-square)](https://github.com/ita-social-projects/Forum-Sandbox/issues)
[![Pending Pull-Requests](https://img.shields.io/github/issues-pr/ita-social-projects/Forum-Sandbox?style=flat-square)](https://github.com/ita-social-projects/Forum-Sandbox/pulls)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- For more on these wonderful  badges, refer to <a href="#" target="_blank">#</a>.

---

## Table of Contents (Optional)

> If your `README` has a lot of info, section headers might be nice.

- [Installation](#installation)
  - [Required to install](#Required-to-install)
  - [Environment](#Environment)
  - [Clone](#Clone)
  - [Setup](#Setup)
  - [How to run local](#How-to-run-local)
  - [How to run Docker](#How-to-run-Docker)
- [Usage](#Usage)
  - [How to work with swagger UI](#How-to-work-with-swagger-UI)
  - [How to run tests](#How-to-run-tests)
  - [How to Checkstyle](#How-to-Checkstyle)
- [Documentation](#Documentation))
- [Contributing](#contributing)
  - [git flow](#git-flow)
  - [issue flow](#git-flow)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

---

## Installation

- All the `code` required to get started
- Images of what it should look like

### Required to install
* Python 3.9
* PostgreSQL 14
* Django 4.2.3
* NodeJS Frontend


### Environment
environmental variables
```properties
#db details
SECRET_KEY= key ...
PG_DB= forum
PG_USER= postgres
PG_PASSWORD= postgres
DB_HOST= localhost
DB_PORT= 5432
DB_PORT_OUT= 55432 # Check if there is a conflict with the setup on port 55432

#pgadmin user
PGADMIN_EMAIL: admin@admin.com
PGADMIN_PASSWORD: key ...

#SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST= someuser@gmail.com
EMAIL_PORT= 587
EMAIL_USE_TLS= 1
EMAIL_HOST_USER= test@test.com
EMAIL_HOST_PASSWORD= test-password

#origin hostnames allowed to make cross-site HTTP requests
CORS_ORIGIN_WHITELIST=
```

### Clone

- Clone this repo to your local machine using `https://github.com/ita-social-projects/Forum-Sandbox.git`

### Setup

- If you want more syntax highlighting, format your code like this:
- Localhost

> update and install this package first

```shell
$ pip install -r requirements.txt
```

> now install npm and bower packages

```shell
$ sudo apt update
$ sudo apt install nodejs
$ sudo apt install npm

```

- For all the possible languages that support syntax highlithing on GitHub (which is basically all of them), refer <a href="https://github.com/github/linguist/blob/master/lib/linguist/languages.yml" target="_blank">here</a>.

### How to run local
- Setup .env
> Setup .env
``` shell
SECRET_KEY= 'key ...'
PG_DB= forum
PG_USER= postgres
PG_PASSWORD= postgres
DB_HOST= localhost
DB_PORT= 5432
DB_PORT_OUT= 5432 # Check if there is a conflict with the setup on port 55432

#pgadmin user
PGADMIN_EMAIL: admin@admin.com
PGADMIN_PASSWORD: key ...

#SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST= someuser@gmail.com
EMAIL_PORT= 587
EMAIL_USE_TLS= 1
EMAIL_HOST_USER= test@test.com
EMAIL_HOST_PASSWORD= test-password

#origin hostnames allowed to make cross-site HTTP requests
CORS_ORIGIN_WHITELIST=
```
- User, run the local server on port localhost:8000
``` shell
$ psql -U postgres -d forum < dump_forum.sql
$ python manage.py runserver
or 
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser (custom_admin_panel_user)
$ python manage.py runserver
```

### How to run Docker

- Setup Docker  
> Setup .env
``` shell
SECRET_KEY= 'key ...'
PG_DB= forum
PG_USER= postgres
PG_PASSWORD= postgres
DB_HOST= db
DB_PORT= 5432
DB_PORT_OUT= 5432 # Check if there is a conflict with the setup on port 55432

#pgadmin user
PGADMIN_EMAIL: admin@admin.com
PGADMIN_PASSWORD: 1

#SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST= someuser@gmail.com
EMAIL_PORT= 587
EMAIL_USE_TLS= 1
EMAIL_HOST_USER= test@test.com
EMAIL_HOST_PASSWORD= test-password
```
> Run Docker comands
```shell
$ docker compose build
$ docker compose up
$ docker exec -i contener-name-exemple python manage.py makemigrations
$ docker exec -i contener-name-exemple python manage.py migrate
or 
$ docker compose build
$ docker compose up
$ docker exec -i forum-sandbox-db-1 psql -U postgres -d forum < dump_forum.sql
```

> Stop Docker comands
```shell
ctrl + c
$ docker stop $(docker ps -q)
```
---

## Usage
### How to work with swagger UI
### How to run tests
- User, run test:
```shell
$ python manage.py test
```

### How to Checkstyle

---

## Documentation
- 🔃 Documentation <a href="https://github.com/ita-social-projects/Forum-Sandbox/wiki" target="_blank">Forum-Sandbox/wiki</a>.

---

## Contributing

### Git flow
> To get started...
#### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/ita-social-projects/Forum-Sandbox.git`

#### Step 2

- **HACK AWAY!** 🔨🔨🔨

#### Step 3

- 🔃 Create a new pull request using <a href="#" target="_blank">https://github.com/ita-social-projects/Forum-Sandbox.git</a>.

### Issue flow

---

## Team

> Or Contributors/People

[![@romanmyko](https://avatars.githubusercontent.com/u/123646984?v=4?s=50)](https://github.com/romanmyko)
[![@ohorodnykostap](https://avatars.githubusercontent.com/u/95187662?v=4?s=200)](https://github.com/ohorodnykostap)
[![@do-androids-dream](https://avatars.githubusercontent.com/u/116935261?v=4?s=200)](https://github.com/do-androids-dream)
[![@Anorhayz](https://avatars.githubusercontent.com/u/70011041?v=4?s=200)](https://github.com/Anorhayz)
[![@GodaimeSan22](https://avatars.githubusercontent.com/u/125042739?v=4?s=200)](https://github.com/GodaimeSan22)
[![@pythonStudent88](https://avatars.githubusercontent.com/u/125041382?v=4?s=200)](https://github.com/pythonStudent88)
 

- You can just grab their GitHub profile image URL
- You should probably resize their picture using `?s=200` at the end of the image URL.

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="#" target="_blank">`#`</a>
- Facebook at <a href="#" target="_blank">`#`</a>
- Insert more social links here.

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://softserve.academy/" target="_blank"> SoftServe IT Academy</a>.
