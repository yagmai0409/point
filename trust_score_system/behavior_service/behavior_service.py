from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_id = data['user_id']
    ip_address = data['ip_address']
    mac_address = data['mac_address']
    login_time = data['login_time']
    
    risk_score = 0
    abnormal_ips = ['192.168.1.1', '10.0.0.1']
    abnormal_macs = ['00:0a:95:9d:68:16', '00:1b:44:11:3a:b7']
    
    if ip_address in abnormal_ips:
        risk_score += 10
    if mac_address in abnormal_macs:
        risk_score += 10
    
    login_hour = datetime.strptime(login_time, '%Y-%m-%d %H:%M:%S').hour
    if login_hour < 6 or login_hour > 22:
        risk_score += 5
    
    return jsonify({'user_id': user_id, 'risk_score': risk_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
