from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    user_id = data['user_id']
    
    # 假設基本的信任分數
    base_trust_score = 100
    
    # 獲取風險分數
    response = requests.get(f'http://behavior_service:5002/analyze/{user_id}')
    risk_score = response.json().get('risk_score', 0)
    
    # 計算最終的信任分數
    trust_score = base_trust_score - risk_score
    return jsonify({'user_id': user_id, 'trust_score': trust_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
