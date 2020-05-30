"""Main entrance to application"""

import connexion

options = {'swagger_ui': False}

# if you don't install ui, you have to disable it
app = connexion.FlaskApp(__name__, port=8080)
app.add_api('swagger.yaml',
            validate_responses=True,
            options=options)

if __name__ == '__main__':
    app.run(debug=True)
