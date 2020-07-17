from flask import Flask, jsonify, request
from PortalsData import PortalsData

app = Flask(__name__)

@app.route('/')
def default():
    return jsonify({'hello' : 'world'})

@app.route('/<string:username>/<string:password>', methods=['GET'])
def get_portals_data(username, password):
    portals_data = PortalsData(username, password)
    teacher_list = portals_data.get_teacher_list()
    return jsonify({'teachers' : teacher_list})

if __name__ == '__main__':
    app.run(debug=True)