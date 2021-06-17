# myurlshortcut
Personal project in django
Thats my first experience in web developing . I had an idea to make simple url cutter with history of searching.
Here i used custom tips of style coding .

![Build Status ](https://github.com/Yurasblv/myurlshortcut/actions/workflows/main.yml/badge.svg?branch=master)

U can easily test that application on your PC ,there are steps for install in your dev tool.

1. Clone repo 
``` bash
git clone https://github.com/Yurasblv/myurlshortcut.git
   ```
2. Run bash commands
Go to projects folder
``` bash 
cd activity
```
Run develop mode
``` bash 
make
```
Apply migrations
```
make migrate
```
Create superuser
```bash make bash

python manage.py createsuperuser

Username: admin
Email address: admin@admin.admin
Password: adminadmin
```
Open started project on browser
``` 
    bash 
    open http://localhost:8000/
```
If you want connect to local database use these credentials:
```
Host: localhost
Port: 5432
User: postgres
Password: supersecretpassword
```

