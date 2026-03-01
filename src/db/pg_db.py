from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


def get_db_url() -> str:
    """postgresql连接字符串"""
    return "postgresql+asyncpg://zhangdezhi:12345678@localhost:5432/knowledge"


engine = create_async_engine(
    get_db_url(),
    pool_size=10,
    pool_recycle=3600,
    max_overflow=20,
    pool_pre_ping=True,
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    try:
        db = async_session()
        yield db
    except Exception as e:
        print(f"数据库操作错误:{e}")
        if db and db.in_transaction():
            await db.rollback()
    finally:
        if db:
            await db.close()
