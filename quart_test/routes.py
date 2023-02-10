from quart import Response, Blueprint
from quart import render_template

bp = Blueprint("bp", __name__)


@bp.route("/")
async def hello():
    div="666"
    return await render_template("token.html",div=div)
