from flask import Flask,render_template,request,redirect,url_for
from bson import ObjectId
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://admin:anusuya123@cluster0.x62chpp.mongodb.net/mydb?retryWrites=true&w=majority"
mongo = PyMongo(app)

Todo= mongo.db.todos
@app.route('/')
def home():
    todo_list = Todo.find()
    return render_template('base.html',todo_list=todo_list)

@app.route('/add',methods=['POST'])
def add():
    new_todo = request.form.get('name')
    Todo.insert_one({'text': new_todo, 'done': False})
    return redirect(url_for("home"))

@app.route('/update')
def update():
    todo_list = Todo.find()
    filter = {'done': False}
    newvalues={"$set": {"done": True}}
    Todo.update_one(filter, newvalues)
    return redirect(url_for("home"))

@app.route('/delete_completed')
def delete_completed():
    Todo.delete_many({'done' : True})
    return redirect(url_for("home"))

@app.route('/delete')
def delete():
    Todo.delete_many({})
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run()









