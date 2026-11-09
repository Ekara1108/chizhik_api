import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CartItem(BaseModel):
    phone: str
    product_id: str
    quantity: int = 1

@app.post("/add_to_cart")
async def add_to_cart(item: CartItem):
    api_key = os.getenv("PROXYAPI_KEY")
    
    # URL, куда ваш сервер будет отправлять запрос к Чижику через ProxyAPI
    # (Точный адрес запроса корзины берется из документации API Чижика)
    chizhik_url = "https://chizhik.ru" 
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "phone": item.phone,
        "product_id": item.product_id,
        "quantity": item.quantity
    }
    
    try:
        # Отправляем запрос в Чижик через шлюз ProxyAPI
        response = requests.post(chizhik_url, json=payload, headers=headers)
        return {"status": "success", "data": response.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

