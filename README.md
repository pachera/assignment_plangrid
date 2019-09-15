https://docs.google.com/document/d/1iEjEtAcvw62s9SypQOyMwTqMBC9Yv2g99No1PEIgyoE/edit#heading=h.k175kgjuqtwk

Prerequisites:

Linux:
httpie (Ubuntu: apt-get install httpie)
python3 (Ubuntu: apt-get install python3)

Python:
python -m pip install --upgrade pip; pip install -r requirements.txt (included)

------------------------------------------
Solution:

Starting Django Server: python manage.py runserver
OR
Debug Mode: LOGLEVEL=DEBUG python manage.py runserver

Output in console:

Debug is enabled!!!
Debug is enabled!!!
Performing system checks...

System check identified no issues (0 silenced).
September 15, 2019 - 00:19:42
Django version 2.2.5, using settings 'mytest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


Expected logging in console and logfile debug.log:

hello_world.views DEBUG    2019-09-15 00:02:10,011 http://127.0.0.1:8000/

hello_world.views DEBUG    2019-09-15 00:02:19,541 http://127.0.0.1:8000/

hello_world.views DEBUG    2019-09-15 00:02:44,712 http://127.0.0.1:8000/

----------------------------------------------------
Testing:

Test 1. http requests by a Linux client (httpie):

Command: http 127.0.0.1:8000

HTTP/1.1 200 OK
Content-Length: 21
Content-Type: text/html; charset=utf-8
Date: Sun, 15 Sep 2019 00:21:53 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

Command: http 127.0.0.1:8000 Accept:application/json
HTTP/1.1 200 OK
Content-Length: 28
Content-Type: application/json
Date: Sun, 15 Sep 2019 00:46:59 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "message": "Hello, World!"
}
-----------------------------------------
Test 2: python script making external requests:

python testmytest.py 127.0.0.1:8000
HTML pass <p>Hello, World!</p>
JSON pass {'message': 'Hello, World!'}

-----------------------------------------
Test 3: django test facilities with mock requests:

cat hello_world/tests_views.py

python manage.py test hello_world -v2

Debug is enabled!!!
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_my_view_html (hello_world.tests_views.RequestTests) ... ok
test_my_view_json (hello_world.tests_views.RequestTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
