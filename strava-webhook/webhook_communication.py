from flask import Flask,request,json

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook_subscription():
    verify_token = "STRAVA_WEATHER_SERVICE" #token strava

    mode = request.args['hub.mode']
    token = request.args['hub.verify_token']
    challenge = request.args['hub.challenge']

    if mode=="subscribe" and token==verify_token:
        print("Webhook verified")
        return {"hub.challenge":challenge}, 200
    else:
        return {"error":"Token verification failed"}, 403

@app.route('/webhook',methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        data = request.json
        print("data received from webhook :", data)
        return data

app.run(host='0.0.0.0', port=8000)