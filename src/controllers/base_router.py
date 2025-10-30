from fastapi import Depends, APIRouter
from src.utils.config import Settings, get_settings



# Initialize the base router
BASE_ROUTER = APIRouter()

# Healthy Check Function
@BASE_ROUTER.get("/", tags=["Healthy"], description="Healthy check endpoint")
async def Home(settings: Settings = Depends(get_settings)):
     return {
          "app_name": settings.APP_NAME,
          "version": settings.VERSION,
          "message": "Welcome to the Sentiment Analysis API"
     }
     