import random
import sys
from FanController import FanController
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

fanController = FanController(10, 12)


@app.route('/')
def index():
    return "Fan Controller BackEnd"


@app.route('/RPM', methods=['GET'])
def get_rpm():
    try:
        rpm = fanController.rpm
        return jsonify({'RPM': rpm})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/DutyCycle', methods=['POST'])
def set_duty_cycle():
    try:
        data = request.get_json()
        duty_cycle = data['DutyCycle']
        fanController.duty_cycle = duty_cycle
        return jsonify({'success': True})
    except Exception as e:
        return jsonify(
            {'success': False},
            {'error': str(e)}), 500


def run_app(host="0.0.0.0", port=5000):
    app.run(host=host, port=port)


if __name__ == '__main__':
    try:
        ip_address = sys.argv[1]
        port_num = sys.argv[2]
        run_app(ip_address, port_num)
    except Exception as e:
        print("Port Setup Failed, using defaults")
        run_app()
