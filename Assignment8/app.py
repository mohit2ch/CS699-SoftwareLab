from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from http import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String(200), nullable=False)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Task {self.id}"
    
# print(datetime.UTC)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        current_task = request.form.get("content", False)
        new_todo = Todo(content=current_task)
        try:
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/')

        except Exception as e:
            print(f'ERROR : {e}')
            return f"ERROR:{e}"
    else:
        tasks = Todo.query.order_by(Todo.date_updated).all()
        return render_template("index.html", tasks=tasks)
    return render_template("index.html")

@app.route("/delete/<int:id>")
def delete(id:int):
    delete_todo = Todo.query.get_or_404(id)
    try:
        db.session.delete(delete_todo)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"ERROR : {e}"

@app.route("/changestatus/<int:id>")
def changestatus(id:int):
    done_todo = Todo.query.get_or_404(id)
    try:
        done_todo.completed += 1
        done_todo.completed = done_todo.completed%2
        done_todo.date_updated = datetime.utcnow()
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import socket
# from http import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String(200), nullable=False)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Task {self.id}"
    
# print(datetime.UTC)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        current_task = request.form.get("content", False)
        new_todo = Todo(content=current_task)
        try:
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/')

        except Exception as e:
            print(f'ERROR : {e}')
            return f"ERROR:{e}"
    else:
        tasks = Todo.query.order_by(Todo.date_updated).all()
        return render_template("index.html", tasks=tasks)
    return render_template("index.html")

@app.route("/delete/<int:id>")
def delete(id:int):
    delete_todo = Todo.query.get_or_404(id)
    try:
        db.session.delete(delete_todo)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"ERROR : {e}"

@app.route("/changestatus/<int:id>")
def changestatus(id:int):
    done_todo = Todo.query.get_or_404(id)
    try:
        done_todo.completed += 1
        done_todo.completed = done_todo.completed%2
        done_todo.date_updated = datetime.utcnow()
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"

def is_port_available(port):
    """Return True if port is free on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("127.0.0.1", port))
            return True
        except OSError:
            return False


if __name__ == "__main__":
    port_number = 5000

    while True:
        try:
            if 1 <= port_number <= 65535:
                if is_port_available(port_number):
                    print(f"Port {port_number} is available.")
                    break
                else:
                    print(f"Port {port_number} is in use.")
            else:
                print("Port must be between 1 and 65535.")

            port_number = int(input("Enter a port number (1-65535): "))

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            port_number = int(input("Enter a port number (1-65535): "))
            

    with app.app_context():
        db.create_all()

    print(f"Starting Flask app on port {port_number}...")
    app.run(port=port_number, debug=True, use_reloader=False)
