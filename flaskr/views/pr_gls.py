from flask import (
    Blueprint, request, current_app, request, abort, json
)

from ..utils import (
    generic_error_handler
)

import oct2py

pr_gls = Blueprint('pr_gls', __name__)


@pr_gls.route('/pr-gls', methods=['POST'])
def pr_gls_interface():
    input_data = request.get_json()

    # Calling PR-GLS static file
    with oct2py.Oct2Py() as oc:
        oc.eval('cd %s/PR-GLS/CPD' % current_app.static_folder)
        oc.eval('mex cpd_P.c')
        oc.eval('mex cpd_Pappmex.c')
        oc.eval('mex cpd_Pcorrespondence.c;')
        oc.eval('cd ..')
        res = oc.feval('prlgdemo')

    # Calling PR-GLS static file
    # with oct2py.Oct2Py() as oc:
    #     oc.eval('cd %s/PR-GLS' % current_app.static_folder)
    #     oc.eval('load ./data/save_fish_def_5_1.mat')
    #     oc.eval('X = x1')
    #     oc.eval('Y = y2a')
    #     x = oc.eval('compute_prgls(X, Y)')
    #     print(x)

    # except oc.utils.Oct2PyError:
    #     abort(500)

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
