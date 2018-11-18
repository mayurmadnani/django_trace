#### Django Trace and Shell support through web socket

##### Project Description

The dev tool can be used in a local or a staging environment where the  error is captured by the middleware and the **error trace is displayed objects are recreated** in an object called 'trace' and can be **debugged  over the online shell available**

Also, a **decorator** that can be enhanced to **trace memory leakages** in  celery tasks and eventually **store it in djcelery** so that can be analyzed  later

Tried chat modules using channels which can be eventually used to run  python commands using WebSocket with the context of the error.

```shell
git clone git@github.com:mayurmadnani/django_trace.git 
pip install -r requirements.txt 
python manage.py migrate 
python manage.py makemigrations chat 
python manage.py migrate python manage.py runserver
```

