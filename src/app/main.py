from fastapi import FastAPI
from app.user.application.user_controller import router as user_router
from app.auth.application.auth_controller import router as auth_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="MS-USERS",
        version="1.0.0",
        description="Microservice for user and auth management"
    )

    app.include_router(user_router, prefix="/users", tags=["Users"])
    app.include_router(auth_router, prefix="/auth", tags=["Auth"])

    return app

app = create_app()
