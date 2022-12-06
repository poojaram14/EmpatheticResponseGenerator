from empathyBot import EmpathyResponse
from flask import Flask, request, jsonify
from flask_cors import CORS

empathic_ai = EmpathyResponse()
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/aiResponse', methods = ['GET','POST'])
def _ai_response():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        user_query = request.json
        return jsonify({'ai_response':empathic_ai.predict(user_query['query'])})
    else:
        return 'Content-Type not supported!'
    

if __name__ == '__main__':
    app.run()