from fastapi import APIRouter
from pydantic import BaseModel

from heimdallr.api.base import serve_channels_async

push_router = APIRouter()


@push_router.get("/{key}/{body}")
@push_router.post("/{key}/{body}")
@push_router.get("/{key}/{title}/{body}")
@push_router.post("/{key}/{title}/{body}")
async def send_push(key: str, title: str = "", body: str = "", msg_type: str = ""):
    return await serve_channels_async(key, title, body, msg_type=msg_type)


class PostRequest(BaseModel):
    key: str = ""
    title: str = ""
    body: str = ""
    msg_type: str = "text"


@push_router.post("/push")
async def send_push_by_json(request: PostRequest):
    return await serve_channels_async(request.key, request.title, request.body, msg_type=request.msg_type)
