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
    print(f'Incoming param id {id}')
    return doc


def create(user, body):
    doc['userId'] = user['id']
    doc['name'] = body['name']
    doc['companyId'] = connexion.request.headers['X-Company-ID']

    return doc, 201
