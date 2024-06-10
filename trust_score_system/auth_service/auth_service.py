from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
   
    if data['username'] == 'user' and data['password'] == 'password':
        return jsonify({'status': 'success', 'user_id': 1})
    else:
        return jsonify({'status': 'failure'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)