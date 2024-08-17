from fastapi import HTTPException, APIRouter

from .models import AddressData
from .settings import REDIS_CONNECT, logger

router = APIRouter()

@router.post("/write_data")
async def write_data(data: AddressData):
    try:
        # Оберзаем +, если есть, т.к. при get запросе FastAPI его обрезает сам
        if data.phone.startswith("+"):
            data.phone = data.phone.replace("+", "")
        # Сохранение данных в Redis
        REDIS_CONNECT.set(data.phone, data.address)
        logger.info(f"Data saved: {data.phone} -> {data.address}")
        return {"message": "Data saved successfully"}
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error")

@router.get("/check_data")
async def check_data(phone: str):
    try:
        # Получение данных из Redis
        address = REDIS_CONNECT.get(phone.strip())
        if address:
            logger.info(f"Data retrieved: {phone} -> {address.decode()}")
            return {"phone": phone, "address": address.decode()}
        else:
            logger.warning(f"Phone number not found: {phone}")
            raise HTTPException(status_code=404, detail=f"Phone number not found {phone}")
    except Exception as e:
        logger.error(f"Error retrieving data: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error")
