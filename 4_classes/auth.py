"""Authorization handler for requests. In fact it gets logged user data from IAM service."""

import connexion
from connexion.exceptions import Unauthorized


def get_auth(token):
    """
    Validates Authorization token (Bearer) via IAM service.
    This method is automatically called by connection for http methods with defined authorization
    in openapi file.
    :param token: Authorization token (from Authorization header_
    :return: RFC7662 compliant dict (with user details under 'sub' key)
    """

    # untill this point, connexion did not yet validated schema!!!
    # if there is no such header it will raise exception
    company_id = connexion.request.headers['X-Company-ID']

    headers = {
        'Authorization': f'Bearer {token}',
        'X-Company-ID': company_id
    }

    # call auth service, get user data
    user_data = post_auth(headers)

    if not user_data:
        raise Unauthorized

    return {
        'scope': 'documents presigned_url',
        'sub': user_data
    }


def post_auth(token: str):
    """
    This function mocks auth service, ie. OpenAuth, IAM, etc
    """

    # some negative path
    if 'bla' in token['Authorization']:
        return None

    return {'name': 'John Rambo', 'id': 'a62a5052-9933-42fa-a235-1c3a078188b1'}
