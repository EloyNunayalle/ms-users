from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.user.dto.user_dto import UserResponseDto

router = APIRouter()

@router.get("/", response_model=list[UserResponseDto])
def list_users():
    mock_users = [
        UserResponseDto(id=1, first_name="Pedro", last_name="Pi", email="pedro@123.edu.pe", role="ADMIN", is_active=True),
        UserResponseDto(id=2, first_name="person", last_name="carnot", email="carnot@utec.edu.pe", role="USER", is_active=True)
    ]
    return JSONResponse(status_code=200, content=[u.model_dump() for u in mock_users])

@router.get("/{user_id}", response_model=UserResponseDto)
def get_user(user_id: int):
    user = UserResponseDto(
        id=user_id,
        first_name="Mock",
        last_name="User",
        email="mock@utec.edu.pe",
        role="USER",
        is_active=True
    )
    return JSONResponse(status_code=200, content=user.model_dump())
