from src.dao.base_dao import BaseDAO
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User


class UserDAO(BaseDAO):

    def __init__(self, db: AsyncSession):
        """"初始化用户对像"""
        super().__init__(db, User)
