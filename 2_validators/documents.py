from uuid import uuid4

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


def create(body):
    name = body['name']

    doc['name'] = name

    return doc, 201
