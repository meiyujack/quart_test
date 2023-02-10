from quart import Quart, render_template, Response
from .routes import bp

app = Quart(__name__)
app.register_blueprint(bp,url_prefix='/bp')

from quart_test import routes


@app.route('/')
@app.route('/index')
async def index():
    return "Hello, World!"


@app.route('/token')
async def token():
    _token = "123"
    response = await render_template("token.html", token=_token)
    headers = {"token": _token}
    return Response(response, headers=headers)


def run():
    app.run()
