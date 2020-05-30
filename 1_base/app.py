import connexion
from flask import render_template

# if you don't install ui, you have to disable it
# add ui by pip3 install connexion[swagger-ui]
options = {'swagger_ui': True}

app = connexion.FlaskApp(__name__, port=8080)
app.add_api('swagger.yaml',
            validate_responses=True,  # check responses
            options=options)


# add undocumented route, its simply a Flask route!
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
