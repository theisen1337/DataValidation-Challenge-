""""

    Author: Thomas Theis, 2021
    This class is used for handling the REST API
    Following PEP8 Style Guide https://www.python.org/dev/peps/pep-0008/

"""

# Third party imports
from flask import Flask, jsonify, request

# Python Standard
import json
# Self made
from BusinessLogic import BusinessLogic as BL

bl = BL('./restaurants.csv')

app = Flask(__name__)


@app.route('/open', methods=['GET', 'POST'])
def api_open():
    # POST request
    if request.method == 'POST':
        """
            Handle REST API POST Call
        """

        try:
            # Test if json is sent from the Browser or requests.
            data = request.get_json().keys()
        except:
            # Data is sent from requests and is a json string.
            data = json.loads(request.get_json())

        # Do Business Logic
        open_list = bl.get_open_restaurants(data['api_call'])

        # Convert list object to json.
        json_dict = {"open": open_list}
        rtn_str = json.dumps(json_dict)
        return rtn_str, 200

    # GET request
    else:
        """
            Handle REST API GET Call
        """
        message = {'message': 'This is not the page you are looking for.'}
        return jsonify(message)  # serialize and use JSON headers


app.run(port=5000)
