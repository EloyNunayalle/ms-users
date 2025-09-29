from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.auth.dto.login_request_dto import LoginRequestDto
from app.auth.dto.auth_response_dto import AuthResponseDto
from app.auth.dto.register_request_dto import RegisterRequestDto


_FAKE_USERS: dict[str, dict] = {}

router = APIRouter()
@router.post("/register", response_model=AuthResponseDto)
def register_user(request: RegisterRequestDto):
    if request.email in _FAKE_USERS:
        return JSONResponse(
            status_code=400,
            content={"status": "error", "message": "Email already registered"}
        )

    _FAKE_USERS[request.email] = {
        "first_name": request.first_name,
        "last_name": request.last_name,
        "password": request.password, 
        "role": "USER",
    }

    response = AuthResponseDto(
        message="User registered successfully",
        email=request.email,
        role="USER"
    )
    return JSONResponse(status_code=201, content=response.model_dump())

@router.post("/login", response_model=AuthResponseDto)
def login_user(request: LoginRequestDto):
    response = AuthResponseDto(
        message="Login successful",
        email=request.email,
        role="USER",              
        token="fake-jwt-token"  
    )
    return JSONResponse(status_code=200, content=response.model_dump())
