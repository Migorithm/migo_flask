## Initialization of app
```python
from flask import Flask
app=Flask(__name__)
```
\_\_name\_\_ is used to determine the location of the application, which in turn allows it to locate other files such as images and templates.

### View functions
```python
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"
```
Tihs registers function ***index()*** as the handler for the application's root URL. Traditionally it was written as follows:

```python
def index():
    return "<h1>Hello World!</h1>"
app.add_url_rule('/','index',index) 
                #URL, endpoint name, view function in order
```

#### Dynamic routes
```python
@app.route('/user/<name>')
def index():
    return "<h1>Hello World!</h1>"
```

### flask run command
This command looks for the name of Python script that contains the application instance in the FLASK_APP environment variable. To start with:
```sh
$ export FLASK_APP=hello.py
$ flask run
```
<br>

Alternatively;
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0",,port=41410,debug=True)
```
Debug mode allows auto-reloading and debugging. But never use debug mode on production server as it allows the client to request remote code exeuction, resulting in vulnerability.

## Request - Response Cycle
