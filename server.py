from flask import Flask, request,jsonify
from datetime import datetime

app = Flask(__name__)


rank = []


@app.route('/rank', methods=['POST'])
def post_rank():
    name = request.json['name']
    time = request.json['time']

    rank.append({'name': name, 'time': datetime.strptime(time, '%M:%S').time()})
    print(rank)
    return '', 201


@app.route('/rank', methods=['GET'])
def view_rank():
    real_rank = sorted(rank, key=lambda item: item['time'])

    return jsonify([{
        'name': data['name'],
        'time': str(data['time'])
    } for data in real_rank]), 200


app.run(port=80)

