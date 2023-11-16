Custom administrative panel of the project. Django 
Superuser rights (can add additional site administrators)
Design and structure of a single filtering page built on slugs

1.1 Statistics tab

- Display of users who registered recently and their quantity...

1.2 Users tab

- With a filtering field (user type)
- With a sorting field by criteria or selected field
- Search field by name (selectable search content) using the selector method
- Pagination with the option to choose the number of items per page

1.3 Full user card with SEO fields

- H2 level tags for the project or card name
- Lower-level tags for descriptions
- CRUD operations on the card

1.4 Access to files with graphical or textual content located in the backend TEMP vs Media folder.

1.5 Database backup (not always direct access to the server). Backup without graphical content.

WEB (UA) based on Django folders (templates + static)

Access path ./domain name/association name with Admin 'can be located at the subdomain level'

1.6 Сomply with security standards
- prohibition on the name in the URL (admin) and any concatenations of it!!!
- login page (email or login) + password (Forgot password => recovery via email)
- captcha (in perspective)

1.7 Security
- prohibition on scanning the site structure (robots.txt file .HttpAccess)
- LogFile display files (critical changes or errors)
- prohibition on the name in the URL (admin) and any concatenations of it!!!
- the superuser can have two levels of security.
- ability to restrict the rights of the superuser (prohibition on backup, etc.)