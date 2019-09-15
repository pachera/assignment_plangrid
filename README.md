https://docs.google.com/document/d/1iEjEtAcvw62s9SypQOyMwTqMBC9Yv2g99No1PEIgyoE/edit#heading=h.k175kgjuqtwk

Prerequisites:

Linux:
httpie (Ubuntu: apt-get install httpie)
python3 (Ubuntu: apt-get install python3)

Python:
python -m pip install --upgrade pip
pip install -r requirements.txt (included)

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

Testing:

Test 1. http requests by a Linux client (hhtpie):

Command: http 127.0.0.1:8000

HTTP/1.1 200 OK
Content-Length: 21
Content-Type: text/html; charset=utf-8
Date: Sun, 15 Sep 2019 00:21:53 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

<p>Hello, World!</p>

Command: http 127.0.0.1:8000
HTTP/1.1 200 OK
Content-Length: 21
Content-Type: text/html; charset=utf-8
Date: Sun, 15 Sep 2019 00:21:53 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

<p>Hello, World!</p>

Test 2:
