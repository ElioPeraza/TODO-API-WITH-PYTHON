from flask import Flask, request, jsonify
app = Flask(__name__)


todo_list = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    },
    {
        "done": False,
        "label": "Sample Todo 3"
    },
    {
        "done": True,
        "label": "Sample Todo 4"
    }
]

@app.route("/")
def hello():
    return "Welcome to my API RESTFUL"

@app.route("/todos/<position>", methods=['GET'])
def get_todos(position):
    return jsonify(todo_list[int(position)])

@app.route("/todos", methods=['GET'])
def get_all_todos():
    return jsonify(todo_list), 200
 

@app.route("/todos", methods=['POST'])
def add_todos():
    body = request.get_json()  # Obtener el request body de la solicitud
    if not body:
        return jsonify({"error":"la solicitud es nula"}),400
    if 'label' not in body:
        return 'Debes especificar label', 400
    if 'done' not in body:
        return 'Debes especificar done', 400
    
    new_todo = {
        "done": body['done'],
        "label": body['label']
    }
    todo_list.append(new_todo)
    return jsonify(new_todo), 201 

@app.route("/todos/<position>", methods=['Delete'])

def delete_todo(position):
    todo_list.pop(int(position))
    return jsonify({"message":"Tarea eliminada exitosamente"}), 200
    
    
        

    


app.run(host='0.0.0.0')