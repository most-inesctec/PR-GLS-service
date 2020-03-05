from flask import (
    Blueprint, request, current_app, request, abort, json
)

from ..utils import (
    generic_error_handler
)

pr_gls = Blueprint('pr_gls', __name__)

@pr_gls.route('/pr-gls', methods=['POST'])
def pr_gls_interface():
    input_data = request.get_json()
    print(input_data)

    # Call PSR

    # Error: abort(xxx)

    return current_app.response_class(
        response=json.dumps(input_data),
        status=200,
        mimetype='application/json'
    )

# Customized Error handlers
@pr_gls.errorhandler(401)
def handle_unauthorized_request(e):
    return generic_error_handler(
        401, "Attempt of unauthorized access to information."
    )


@pr_gls.errorhandler(400)
def handle_bad_request(e):
    return generic_error_handler(
        400, "Invalid data passed in request"
    )
