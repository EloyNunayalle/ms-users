from pydantic import BaseModel, EmailStr

class UserResponseDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    role: str
    is_active: bool
