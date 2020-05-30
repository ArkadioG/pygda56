"""Main entrance to application"""

import connexion
from connexion.resolver import RestyResolver

options = {'swagger_ui': False}

# if you don't install ui, you have to disable it
app = connexion.FlaskApp(__name__, port=8080)
app.add_api('swagger.yaml',
            validate_responses=True,
            strict_validation=True,
            options=options,
            resolver=RestyResolver(default_module_name='api',
                                   # GET returning colection must have name other than 'get'
                                   collection_endpoint_name='search')
            )

if __name__ == '__main__':
    app.run(debug=True)
