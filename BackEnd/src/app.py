""" Flask App"""
import sys

from flask import Flask, request, jsonify
from flask_cors import CORS

from fan_controller_mock import FanControllerMock


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
        duty_cycle = data['duty_cycle']
        FAN_CONTROLLER.duty_cycle = duty_cycle
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
    try:
        if 'mock' in sys.argv:
            print("Using Mock Fan Controller")
            FAN_CONTROLLER = FanControllerMock()
        else:
            print("Using Real Fan Controller")
            try:
                from fan_controller import FanController
                FAN_CONTROLLER = FanController(37, 35)
            except ImportError as e:
                print("Unable to import FanController")
                sys.exit(1)
        IP_ADDRESS = sys.argv[1]
        PORT_NUM = sys.argv[2]
        run_app(IP_ADDRESS, PORT_NUM)
    except Exception as e:
        print("Port Setup Failed, using defaults")
        run_app()
