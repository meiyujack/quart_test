from quart import Quart

app=Quart(__name__)


from quart_test import routes

def run():
    app.run()