import random
import sys
from FanControllerMock import FanControllerMock
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
fanController = None


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
        rpm = fanController.rpm
        return jsonify({'RPM': rpm})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/DutyCycle', methods=['POST'])
def set_duty_cycle():
    """ Set Duty Cycle Endpoint

    Returns:
        dict: JSON object with success status and error message if applicable
    """
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
            fanController = FanControllerMock()
        else:
            print("Using Real Fan Controller")
            try:
                from FanController import FanController
                fanController = FanController(18, 23)
            except Exception as e:
                print("Unable to import FanController")
                sys.exit(1)
        ip_address = sys.argv[1]
        port_num = sys.argv[2]
        run_app(ip_address, port_num)
    except Exception as e:
        print("Port Setup Failed, using defaults")
        run_app()
