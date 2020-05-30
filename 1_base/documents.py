from uuid import uuid4

doc = {
    "id": str(uuid4()),
    "name": '',
    "userId": str(uuid4()),
    "companyId": str(uuid4()),
    "uploadDestination": 's3/somebucket'
}

# names of the handler functions can be anything
def get_all():
    # return []
    return "document" # type invalid will cause validation error


def get_details(id):
    print(f'Incoming param id {id}')
    return doc


def create(body):
    name = body['name']

    doc['name'] = name

    # return Response object or standard Flask tuple
    return doc, 201, {'x-custom-header': 'PyGda is cool'}
