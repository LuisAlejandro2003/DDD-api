from fastapi import FastAPI
from shared.api.error_handlers import register_error_handlers
from users.api.router import router as users_router

def create_app() -> FastAPI:
    app = FastAPI(title="API (template DDD)")
    app.include_router(users_router)
    register_error_handlers(app)
    
    return app

app = create_app()
