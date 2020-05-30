from uuid import uuid4

import connexion

doc = {
    "id": str(uuid4()),
    "name": '',
    "userId": str(uuid4()),
    "companyId": str(uuid4()),
    "uploadDestination": 's3/somebucket'
}


class DocumentsView:
    """Semantically like flask's MethodViews"""

    def get_all(self):
        """For collection endpoints choose one name across views - GET can be used only once"""
        return []

    def get(self, id):
        print(f'Incoming param id {id}')
        return doc

    def post(self, user, body):
        doc['userId'] = user['id']
        doc['name'] = body['name']
        doc['companyId'] = connexion.request.headers['X-Company-ID']

        return doc, 201
