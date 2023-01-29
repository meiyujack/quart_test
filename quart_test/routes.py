from quart_test import app


@app.route('/')
@app.route('/index')
async def index():
    return "Hello, World!"
