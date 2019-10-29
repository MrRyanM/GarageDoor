import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
button = 40
GPIO.setmode(GPIO.BOARD)

@app.route("/")
def index():
   return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'pressed':
        if deviceName == 'button':
            relay = button
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay, GPIO.OUT)
        GPIO.output(relay, GPIO.LOW)
        time.sleep(1)
        GPIO.output(relay, GPIO.HIGH)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
