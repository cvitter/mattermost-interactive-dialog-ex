from flask import Flask
from flask import request
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/report", methods=['POST'])
def slash_command():
    """
    Retrieve text field from the form request which contains
    the message entered by the user who invoked the slash command
    """
    form_text = request.form["text"]
    
    if len(form_text) > 0:
        data = {
            "response_type": "in_channel",
            "text": "My response",
        }
    else:
        """
        If the user didn't type a message send a note that only
        they see about typing a message
        """
        data = {
            "response_type": "ephemeral",
            "text": "Error: No status message entered. Please try again.",
        }

    """
    Create the response object to send to Mattermost with the
    data object written as json, 200 status, and proper mimetype
    """
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=False)
