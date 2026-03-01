from typing import List, Type, TypeVar, Generic
from pydantic import BaseModel

from src.dao.base_dao import BaseDAO

DTOType = TypeVar("DTOType", bound=BaseModel)


class BaseService(Generic[DTOType]):
    def __init__(self, dao: BaseDAO, dto_class: Type[DTOType]):
        """
        初始化BaseService
        :param dao: 数据库访问对像(DAO)
        :param dto_class:数据库传输对像(DTO)类
        """
        self.dao = dao
        self.dto_class = dto_class

    async def create(self, **kwargs) -> DTOType:
        """通用创建方法"""
        instance = await self.dao.create(**kwargs)
        return self.dto_class.model_validate(instance)

    async def batch_create(self, objects: List[DTOType]) -> List[DTOType]:
        """批量创建方法"""
        instances = await self.dao.batch_create(objects)
        return [self.dto_class.model_validate(instance) for instance in instances]

    async def get_by_id(self, id) -> DTOType | None:
        """通过主键获取记录"""
        instance = await self.dao.get_by_primary_key(id)
        if instance:
            return self.dto_class.model_validate(instance)
        return None

    async def get_all(self) -> list[DTOType]:
        """"获取所有记录"""
        instances = await self.dao.get_all()
        try:
            if instances:
                return [self.dto_class.model_validate(instance) for instance in instances]
        except Exception as e:
            print(e)
            raise
        return []

    async def update_by_id(self, id,**kwargs) -> DTOType | None:
        """通用更新方法"""
        instance = await self.dao.update_by_primary_key(id, **kwargs)
        if instance:
            return self.dto_class.model_validate(instance)
        return None

    async def delete_by_id(self, id) -> DTOType | None:
        """通过删除方法"""
        instance = await self.dao.delete_by_primary_key(id)



