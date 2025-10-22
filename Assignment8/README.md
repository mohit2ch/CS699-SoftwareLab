## Web Development Assigment

Used Flask framework to deploy a website and provide backend APIs. Used jinja for dynamic html pages. 

### About the Website
The website is a simple Todo List. The functionalities provided are mentioned below.
1. You may add todos and they will be ordered by the time they were last updated
2. Each todo has the following information on display : Date created/repeated and content
3. You may mark the todo as done once the task at hand is complete. The task will now be shown under Done section
4. Done keeps a history of your tasks. You may choose to repeat any of the tasks by clicking repeat. 

### How to setup this project

**Create and activate a virtual environment**
```
$ tar -xf Assignment8.tar.gz
$ cd Assignment8
$ python3 -m venv env
$ source env/bin/activate
```

**Install required libraries**
```
$ pip install -r libraries_required.txt
```

**Start the flask application**
```
python app.py  
Port 5000 is in use.  
Enter a port number (1-65535): 5050  
Port 5050 is available.  
Starting Flask app on port 5050...  
* Serving Flask app 'app'  
* Debug mode: on  
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server inste  
ad.  
* Running on http://127.0.0.1:5050  
Press CTRL+C to quit
```

Now the flask app will be running on http://127.0.0.1:5000 or another user defined port

