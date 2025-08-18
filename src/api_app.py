from fastapi import FastAPI
from users.api.router import router as users_router
from shared.api.error_handlers import register_error_handlers

def create_app() -> FastAPI:
    app = FastAPI(title="Identity API (learning DDD)")
    app.include_router(users_router)
    register_error_handlers(app) 
    return app

app = create_app()
