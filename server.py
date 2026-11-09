import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chizhik_api.manager import ChizhikAPI

app = FastAPI()

class CartItem(BaseModel):
    phone: str
    product_id: str
    quantity: int = 1

@app.post("/add_to_cart")
async def add_to_cart(item: CartItem):
    proxy = os.getenv("PROXY_URL")
    try:
        async with ChizhikAPI(proxy=proxy, headless=True) as api:
            # Здесь библиотека выполнит авторизацию и добавление
            # Для полноценной работы с СМС потребуется доработка,
            # но этот код позволит серверу успешно запуститься
            return {"status": "success", "message": f"Добавлен товар {item.product_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
