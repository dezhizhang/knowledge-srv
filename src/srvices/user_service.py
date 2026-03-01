from sqlalchemy.ext.asyncio import AsyncSession
from src.dao.user_dao import UserDAO
from src.dto.user_dto import UserDto
from src.srvices.base_service import BaseService

class UserService(BaseService):

    def __init__(self, db: AsyncSession):
        super().__init__(UserDAO(db), UserDto)