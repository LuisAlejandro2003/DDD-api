from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

# Sacar DATABASE_URL como env vars
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/n8n"

engine = create_async_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
