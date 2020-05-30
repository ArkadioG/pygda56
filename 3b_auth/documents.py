from uuid import uuid4

import connexion

doc = {
    "id": str(uuid4()),
    "name": '',
    "userId": str(uuid4()),
    "companyId": str(uuid4()),
    "uploadDestination": 's3/somebucket'
}


def get_all():
    return []


def get_details(id):

    # custom error in http-problem format
    # (https://tools.ietf.org/html/draft-ietf-appsawg-http-problem-00)
    if '7' in id:
        return connexion.problem(401, 'Authentication invalid', 'Auth servers said you\'re invalid')

    print(f'Incoming param id {id}')
    return doc


def create(user, body):
    doc['userId'] = user['id']
    doc['name'] = body['name']
    doc['companyId'] = connexion.request.headers['X-Company-ID']

    return doc, 201
