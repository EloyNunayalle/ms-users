from pydantic import BaseModel, EmailStr

class RegisterRequestDto(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
