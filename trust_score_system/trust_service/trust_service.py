from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    user_id = data['user_id']
    ip_address = data['ip_address']
    mac_address = data['mac_address']
    login_time = data['login_time']
    
    base_trust_score = 100
    
    analysis_data = {
        'user_id': user_id,
        'ip_address': ip_address,
        'mac_address': mac_address,
        'login_time': login_time
    }
    response = requests.post('http://behavior_service:5002/analyze', json=analysis_data)
    risk_score = response.json().get('risk_score', 0)
    
    trust_score = base_trust_score - risk_score
    return jsonify({'user_id': user_id, 'trust_score': trust_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
