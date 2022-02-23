# Online System
# Flexy
In this course we shall be building an online system called Flexy

Task 1:
create an isolated environment
```python
python3 -m venv env
```
Task 2:
activate your virtual environment
```python
source env/bin/activate
```

Task 3:
install django, because I have already set up the requirements for you
perform the following command
```python
python -m pip install -r requirements.txt
```

Task 4:
spin up your first project
```python
django-admin startproject flexy
```

Task 5:
migrate your models into your database schema
```python
cd flexy
python manage.py migrate 
```

Task 6:
our system shall have a blog so let us create an application called blog
```python
python manage.py startapp blog
```

Task 7:
view the system interface after performing the following command
```python
python manage.py runserver
```

Once completed push code and create a pull request so that I may be notified