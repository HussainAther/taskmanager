from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

# API route for creating a task
@app.route('/tasks', methods=['POST'])
def create_task():
    description = request.json.get('description')
    due_date = request.json.get('due_date')
    user_id = request.json.get('user_id')

    new_task = Task(description=description, due_date=due_date, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully'}), 201

# API route for reading all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()

    task_list = []
    for task in tasks:
        task_data = {
            'id': task.id,
            'description': task.description,
            'due_date': task.due_date,
            'user_id': task.user_id
        }
        task_list.append(task_data)

    return jsonify(task_list), 200

# API route for updating a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'message': 'Task not found'}), 404

    description = request.json.get('description')
    due_date = request.json.get('due_date')
    user_id = request.json.get('user_id')

    task.description = description
    task.due_date = due_date
    task.user_id = user_id

    db.session.commit()

    return jsonify({'message': 'Task updated successfully'}), 200

# API route for deleting a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run()

