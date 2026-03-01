from fastapi import APIRouter,Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.api_contract import APIContract
from src.db.pg_db import get_db
from src.srvices.user_service import UserService
from src.utils.logger import get_logger


logger = get_logger(__name__)


router = APIRouter(tags=["chat"], prefix="/chat")

class ChatRequest(BaseModel):
    user_id: str
    message: str
    collection_id: str




@router.post("/")
async def chat_with_user(req: ChatRequest, db: AsyncSession = Depends(get_db)):
    logger.info(f"用户信息:{req.user_id} col:{req.collection_id} 消息：{req.message}")
    user_service = UserService(db)
    user = await user_service.get_by_id(req.user_id)
    if not user:
        return APIContract.error(400,"user not found")

    logger.info(f"用户信息:{user}")

    chat_model_handler = C





