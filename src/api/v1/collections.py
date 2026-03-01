from datetime import datetime,timezone
import uuid
from idlelib.window import add_windows_to_menu

from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.api_contract import APIContract
from src.db.pg_db import get_db
from src.srvices.base_service import BaseService

router = APIRouter(tags=["collections"],prefix="/collections")

@router.post("/")
async def create(data:dict,db: AsyncSession = Depends(get_db)):
    service = BaseService(db)
    return APIContract.success()
