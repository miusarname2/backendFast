from fastapi import FastAPI
from routes.home import router as home_router
from routes.users import router as users_router

app = FastAPI()

# --- Incluir routers ---
# Cada router agrupa endpoints relacionados.
# Para agregar más endpoints:
#   1. Crea un archivo en routes/ (ej: routes/products.py)
#   2. Define un router con: router = APIRouter()
#   3. Agrégalo aquí con: app.include_router(products_router, prefix="/products")

app.include_router(home_router)
app.include_router(users_router, prefix="/users")