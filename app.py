#import required libraries
from flask import Flask, request, render_template, jsonify
import json
from flask_cors import cross_origin
# from backend.empathyBot import EmpathyResponse
from backend.empathyBot import EmpathyResponse

empathic_ai = EmpathyResponse()
app = Flask(__name__)
cross_origin(app)
#instantiate flask

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query = (json_)
     prediction = empathic_ai.predict(query)
     return jsonify({'prediction': list(prediction)})
     
# geting and sending response to dialogflow
@app.route('/webhook', methods=['GET' , 'POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    query = req["queryResult"]
    query1 = query["queryText"]
    print(query1)

    fulfillmentText = empathic_ai.predict(query1)

    return {
        "fulfillmentText": fulfillmentText
        # "fulfillmentText": "Response coming from webhook"
    }

if __name__ == '__main__':
    app.debug = True
    app.run()