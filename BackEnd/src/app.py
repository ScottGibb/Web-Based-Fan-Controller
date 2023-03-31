""" Flask App"""
import sys

from flask import Flask, request, jsonify
from flask_cors import CORS

from fan_controller_mock import FanControllerMock
from fan_controller import FanController


app = Flask(__name__)
CORS(app)
FAN_CONTROLLER = None


@app.route('/')
def index():
    """ Index Page route

    Returns:
        str: HTML content for the index page
    """
    return "Fan Controller BackEnd"


@app.route('/RPM', methods=['GET'])
def get_rpm():
    """ Get RPM route

    Returns:
        dict: JSON object containing the current RPM of the fan
    """
    try:
        rpm = FAN_CONTROLLER.rpm
        return jsonify({'RPM': rpm})
    except Exception as exception:
        return jsonify({'error': str(exception)})


@app.route('/DutyCycle', methods=['POST'])
def set_duty_cycle():
    """ Set Duty Cycle Endpoint

    Returns:
        dict: JSON object with success status and error message if applicable
    """
    try:
        data = request.get_json()
        duty_cycle = data['DutyCycle']
        FAN_CONTROLLER.duty_cycle = int(duty_cycle)
        print("Received Duty Cycle: " + str(duty_cycle))
        print(data)
        return jsonify({'success': True})

    except Exception as exception:
        return jsonify(
            {'success': False},
            {'error': str(exception)}), 500


def run_app(host="0.0.0.0", port=5000):
    """ Runs the Flask app

    Args:
        host (str): The hostname for the Flask app
        port (int): The port number for the Flask app
    """
    app.run(host=host, port=port)


if __name__ == '__main__':
    print("Script Arguments:")
    for var in sys.argv:
        print(var)

    if len(sys.argv) == 3:
        print("Server arguments provided")
        ip_address = sys.argv[1]
        port = sys.argv[2]
        FAN_CONTROLLER = FanController(37, 35)
        run_app(ip_address, port)
    elif len(sys.argv) == 2:
        if 'mock' in sys.argv:
            print("Using Mock Fan Controller")
            FAN_CONTROLLER = FanControllerMock()
            run_app()
    else:
        print("Using Default Arguments")
        FAN_CONTROLLER = FanController(37, 35)
        run_app()
