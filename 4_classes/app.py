"""Main entrance to application"""

import connexion
from connexion.resolver import MethodViewResolver

options = {'swagger_ui': True}

# if you don't install ui, you have to disable it
app = connexion.FlaskApp(__name__, port=8080)
app.add_api('swagger.yaml',
            validate_responses=True,
            options=options,
            # custom resolver - no need to declare operationId in the specs!
            resolver=MethodViewResolver(default_module_name='documents',
                                        collection_endpoint_name='get_all'))

if __name__ == '__main__':
    app.run(debug=True)
