from uuid import UUID

import connexion
from connexion.exceptions import Unauthorized
from requests.exceptions import HTTPError
from werkzeug.exceptions import BadRequest, PreconditionFailed

# authorization function can be given in OpenAPI file as path to auth function
# or you can provide it via env var.
# you can also provide url (in OpenAPI file or env var) and Connexion will call it to validate token

def get_auth(token):
    """
    Validates Authorization token (Bearer) via some auth service.
    This method is automatically called by connection for http methods with defined authorization
    in openapi file.
    :param token: Authorization token (from Authorization header_
    :return: RFC7662 compliant dict (with user details under 'sub' key)
    """
    # here you call other auth service to validate token
    user_data = {'name': 'John Rambo', 'id': 'a62a5052-9933-42fa-a235-1c3a078188b1'}

    # RFC7662 compliant dict (with user details under 'sub' key)
    auth_data = {
        'scope': 'documents presigned_url',
        'sub': user_data  # this key can be passed to handler as user
    }

    return auth_data


def get_auth_with_validation(token):
    """
    Validates Authorization token (Bearer) via auth service.
    This method is automatically called by connection for http methods with defined authorization
    in openapi file.
    :param token: Authorization token (from Authorization header_
    :return: RFC7662 compliant dict (with user details under 'sub' key)
    """
    try:
        company_id = connexion.request.headers['X-Company-ID']
        UUID(company_id)  # try to parse to see if valid uuid, connexion validates it after auth

        # some external validation
        user_data = 'call to external validator'

        return {
            'scope': 'documents presigned_url',
            'sub': user_data
        }
    except (TypeError, ValueError):
        raise BadRequest(
            description='All ids in request, whether params or in-body, must be valid UUID.')
    except KeyError:
        raise PreconditionFailed(description='Missing X-Company-ID header.')
    except HTTPError as ex:
        msg = ex.response.json().get('message')
        err_msg = msg if msg else ex.response.text
        raise Unauthorized(err_msg)
