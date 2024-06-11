from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/trust_score', methods=['POST'])
def trust_score():
    auth_data = request.json
    
    auth_response = requests.post('http://auth_service:5001/authenticate', json=auth_data)
    if auth_response.status_code != 200:
        return jsonify({'error': 'Authentication failed'}), 401
    
    user_id = auth_response.json()['user_id']
    ip_address = auth_data.get('ip_address')
    mac_address = auth_data.get('mac_address')
    login_time = auth_data.get('login_time')
    
   
    trust_data = {
        'user_id': user_id,
        'ip_address': ip_address,
        'mac_address': mac_address,
        'login_time': login_time
    }
    trust_response = requests.post('http://trust_service:5003/calculate', json=trust_data)
    trust_score = trust_response.json().get('trust_score', 0)
    
    return jsonify({'user_id': user_id, 'trust_score': trust_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
