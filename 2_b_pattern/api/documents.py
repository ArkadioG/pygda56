from uuid import uuid4

doc = {
    "id": str(uuid4()),
    "name": '',
    "userId": str(uuid4()),
    "companyId": str(uuid4()),
    "uploadDestination": 's3/somebucket'
}


def search():
    """this function handles GET /documents endpoint"""
    return []


def get(id):
    """this function handles GET /documents/{id} endpoint"""
    print(f'Incoming param id {id}')
    return doc


def post(body):
    """this function handles POST /documents endpoint"""
    name = body['name']

    doc['name'] = name

    return doc, 201
