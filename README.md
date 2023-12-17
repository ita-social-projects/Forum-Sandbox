<a href="https://softserve.academy/"><img src="https://s.057.ua/section/newsInternalIcon/upload/images/news/icon/000/050/792/vnutr_5ce4f980ef15f.jpg" title="SoftServe IT Academy" alt="SoftServe IT Academy"></a>

***INSERT GRAPHIC HERE (include hyperlink in image)***

# Repository Title Goes Here

> Subtitle or Short Description Goes Here

> ideally one sentence

> include terms/tags that can be searched

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

[![Build Status](https://img.shields.io/travis/ita-social-projects/GreenCity/master?style=flat-square)](https://travis-ci.org/github/ita-social-projects/GreenCity)
[![Coverage Status](https://img.shields.io/gitlab/coverage/ita-social-projects/GreenCity/master?style=flat-square)](https://coveralls.io)
[![Github Issues](https://img.shields.io/github/issues/ita-social-projects/GreenCity?style=flat-square)](https://github.com/ita-social-projects/GreenCity/issues)
[![Pending Pull-Requests](https://img.shields.io/github/issues-pr/ita-social-projects/GreenCity?style=flat-square)](https://github.com/ita-social-projects/GreenCity/pulls)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- For more on these wonderful  badges, refer to <a href="https://shields.io/" target="_blank">shields.io</a>.

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
SECRET_KEY= 1111
PG_DB= forum
PG_USER= postgres
PG_PASSWORD= postgres
DB_HOST= localhost
DB_PORT= 5432
DB_PORT_OUT= 55432 # Check if there is a conflict with the setup on port 55432

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
$ 
```

> now install npm and bower packages

```shell
$ sudo apt update
$ sudo apt install nodejs
$ sudo apt install npm

```
-Docker run 

- For all the possible languages that support syntax highlithing on GitHub (which is basically all of them), refer <a href="https://github.com/github/linguist/blob/master/lib/linguist/languages.yml" target="_blank">here</a>.

### How to run local

### How to run Docker

---

## Usage
### How to work with swagger UI
### How to run tests
### How to Checkstyle

---

## Documentation

---

## Contributing

### Git flow
> To get started...
#### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/ita-social-projects/SOMEREPO.git`

#### Step 2

- **HACK AWAY!** 🔨🔨🔨

#### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/ita-social-projects/SOMEREPO/compare/" target="_blank">github.com/ita-social-projects/SOMEREPO</a>.

### Issue flow

---

## Team

> Or Contributors/People

[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam) 
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)
[![@lhalam](https://avatars3.githubusercontent.com/u/3837059?s=100&v=4)](https://github.com/lhalam)  

- You can just grab their GitHub profile image URL
- You should probably resize their picture using `?s=200` at the end of the image URL.

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://Website.com" target="_blank">`Website.com`</a>
- Facebook at <a href="https://www.facebook.com/LiubomyrHalamaha/" target="_blank">`Liubomyr Halamaha`</a>
- Insert more social links here.

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://softserve.academy/" target="_blank"> SoftServe IT Academy</a>.