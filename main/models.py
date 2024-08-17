from pydantic import BaseModel, validator
import re


class AddressData(BaseModel):
    phone: str
    address: str

    @validator('phone')
    def phone_must_match_pattern(cls, v):
        # Регулярное выражение для проверки номера телефона
        pattern = r'^(?:\+7|7|8)\d{10}$'
        if not re.match(pattern, v):
            raise ValueError('Phone number must start with +7, 7, or 8 and contain 10 digits')
        return v