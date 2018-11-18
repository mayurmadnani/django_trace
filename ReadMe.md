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

```python
ZeroDivisionError
ZeroDivisionError('division by zero',)
Traceback (most recent call last):
  File "/home/ude/anaconda3/envs/dj-trace/lib/python3.6/site-packages/django/core/handlers/base.py", line 126, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/ude/django_trace/src/chat/decorators.py", line 7, in wrap
    return function(request, *args, **kwargs)
  File "/home/ude/django_trace/src/chat/views.py", line 79, in create_error
    cfat = 10/0
ZeroDivisionError: division by zero
Is the error
{'d': 10, 'c': 6, 'a': 5, 'context_data': 'Hello', 'request': <AsgiRequest: GET '/create_error/'>}
> /home/ude/django_trace/src/sober/middleware.py(23)process_exception()
     22         import ipdb; ipdb.set_trace();
---> 23         return None
     24 

ipdb> trace.context_data                                                                                                                                          
'Hello'
ipdb>  
             
```

**As you can see the above shell opens up only if the error occured and you can get the context in trace object.**

url which caused the error: http://127.0.0.1:8000/create_error/ 

```python
[ Top 10 differences ]
/home/ude/django_trace/src/chat/decorators.py:6: size=136 B (+136 B), count=1 (+1), average=136 B
/home/ude/anaconda3/envs/dj-trace/lib/python3.6/tracemalloc.py:387: size=96 B (+96 B), count=2 (+2), average=48 B
/home/ude/anaconda3/envs/dj-trace/lib/python3.6/tracemalloc.py:524: size=56 B (+56 B), count=1 (+1), average=56 B
/home/ude/anaconda3/envs/dj-trace/lib/python3.6/tracemalloc.py:281: size=40 B (+40 B), count=1 (+1), average=40 B

```

**As you can see the above the traces of memory differences before and after the API ended to show how much memory increased indicating a memory leak in your API or task**