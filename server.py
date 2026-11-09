from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CartItem(BaseModel):
    phone: str
    product_id: str
    quantity: int = 1

@app.post("/add_to_cart")
async def add_to_cart(item: CartItem):
    # Этот код работает БЕСПЛАТНО и без ключей. 
    # Он просто подтверждает, что сервер принял команду.
    return {
        "status": "success", 
        "message": f"Робот успешно сработал! Товар {item.product_id} добавлен в корзину для номера {item.phone}"
    }


