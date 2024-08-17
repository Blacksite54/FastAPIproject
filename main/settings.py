import os
import logging

from fastapi import FastAPI, APIRouter

import redis

DEBUG = True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="My FastAPI App",
    description="API documentation",
    version="1.0.0",
)
router = APIRouter()

REDIS_HOST: str = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT: int = int(os.environ.get("REDIS_PORT", "6379"))

REDIS_CONNECT = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
