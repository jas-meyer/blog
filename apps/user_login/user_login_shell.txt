(djangoEnv) Jasons-MacBook-Pro:blog jasonmeyer$ python manage.py makemigrations
Migrations for 'user_login':
  apps/user_login/migrations/0001_initial.py:
    - Create model User
(djangoEnv) Jasons-MacBook-Pro:blog jasonmeyer$ python manage.py makemigrations
No changes detected
(djangoEnv) Jasons-MacBook-Pro:blog jasonmeyer$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, user_login
Running migrations:
  Rendering model states... DONE
  Applying user_login.0001_initial... OK
(djangoEnv) Jasons-MacBook-Pro:blog jasonmeyer$ python manage.py shell
Python 2.7.10 (default, Oct 23 2015, 19:19:21) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from apps.user_login.models import *
>>> blog.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'blog' is not defined
>>> user.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'user' is not defined
>>> users.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'users' is not defined
>>> user.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'user' is not defined
>>> user.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'user' is not defined
>>> form apps.user_id.models
  File "<console>", line 1
    form apps.user_id.models
            ^
SyntaxError: invalid syntax
>>> from apps.user_id.models import *
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: No module named user_id.models
>>> from apps.user_login.models import *
>>> User.objects.all()
<QuerySet []>
>>> User.object.last()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'User' has no attribute 'object'
>>> User.objects.last()
>>> User.objects.all()
<QuerySet []>
>>> User.objects.last()
>>> Blog.objects.create(first_name = "Woody", last_name ="Woodpecker", email_address = "Ilovewood@gmail.com", age = 105)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Blog' is not defined
>>> User.objects.create(first_name = "Woody", last_name ="Woodpecker", email_address 
<User: User object>
>>> User.objects.all()
<QuerySet [<User: User object>]>
>>> User.objects.last()                                                         <User: User object>
>>> User.objects.create(first_name = "Marty", last_name ="McFly", email_address = "Back@gmail.com",age=18) 
  File "<console>", line 1
    User.objects.create(first_name = "Marty", last_name ="McFly", email_address = "Back@gmail.com",age=18) = 105)
                                                                                                                ^
SyntaxError: invalid syntax
>>> User.objects.create(first_name = "Marty", last_name ="McFly", email_address = "Back@gmail.com",age=18)
<User: User object>
>>> User.objects.create(first_name = "Steve", last_name ="Jobs", email_address = "apple@gmail.com",age=1018)
<User: User object>
>>> User.objects.first()
<User: User object>
>>> User.objects.order_by("first_name")
<QuerySet [<User: User object>, <User: User object>, <User: User object>]>
>>> User.objects.get(id=3)
<User: User object>
>>> User.objects.last()
<User: User object>
>>> User.objects.name
u'objects'
>>> User.objects.last_name
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'last_name'
>>> b = User.object.get(id=3)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'User' has no attribute 'object'
>>> b = User.objects.get(id=3)
>>> b.last_name
u'Jobs'
>>> b. last_name = "Woz"
>>> b.save()
>>> b = User.objects.get(id=3)
>>> b.last_name
u'Woz'
>>> User.objects.create(first_name = "Steve", last_name ="Martin", email_address = "jerk@gmail.com",age=71)
<User: User object>
>>> b =User.objects.get(id=4)
>>> b.last_name
u'Martin'
>>> b.delete()
(1, {u'user_login.User': 1})
>>> User.objects.all()                                                          <QuerySet [<User: User object>, <User: User object>, <User: User object>]>
>>> 
