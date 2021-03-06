import uuid

from sanic import Sanic
from config import CONFIG
from src.router import bp
from sanic_openapi import swagger_blueprint

from src.utils.logUtils import logging_config

app = Sanic(__name__)


@app.middleware('request')
async def set_request_id(request):
    request.headers.update({'X-Request-ID': str(uuid.uuid4())})

app.blueprint(bp)
app.config.from_object(CONFIG)

# add swagger
app.blueprint(swagger_blueprint)

# add logger
logging_config(CONFIG.LOG_ROTATION, CONFIG.LOG_RETENTION)
