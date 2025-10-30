from fastapi import FastAPI
from src.controllers.app_router import APP_ROUTER
from src.controllers.base_router import BASE_ROUTER

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis using various ML models",
    version="1.0.0"
)

# Include routers
app.include_router(BASE_ROUTER)
app.include_router(APP_ROUTER)
