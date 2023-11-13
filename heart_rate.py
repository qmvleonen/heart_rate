from flask import Flask, jsonify, request
app = Flask(__name__)
heart_rate = [
    {
        "Heart_id": "Patient Leonen",
        "Date": ["November 13, 2023"],
        "Heart_rate": ["100"],
    },
]

@app.route('/heart_rate', methods=['GET'])
def getheart_rate():
    return jsonify(heart_rate)

@app.route('/heart_rate', methods=['POST'])
def add_movie():
    movie = request.get_json()
    heart_rate.append(movie)
    return {'id': len(heart_rate)}, 200

@app.route('/heart_rate/<int:index>', methods=['DELETE'])
def delete_heart_rate(index):
    heart_rate.pop(index)
    return 'The heart Rate Has Been Deleted', 200

if __name__=='__main__':
    app.run()
