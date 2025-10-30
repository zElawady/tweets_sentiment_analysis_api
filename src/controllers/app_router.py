from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import APIKeyHeader
from src.utils.inference import TextClassifier
from src.utils.config import Settings, get_settings
from src.models.input_output_schema import text_request, PredictionResponse






# Initialize the TextClassifier
text_classifier = TextClassifier(model_type="glove", model_name="svm")



# Initialize the app router
APP_ROUTER = APIRouter(
     prefix="/predict",
     tags=["Predict"],
     
)


# Verify the Secret api key
api_key_header = APIKeyHeader(name="X-API-Key")
async def verify_api_key(api_key: str = Depends(api_key_header), settings: Settings = Depends(get_settings)):
    if api_key != settings.API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key






@APP_ROUTER.post(path="/", description="Predict sentiment", response_model=PredictionResponse)
async def Predict(texts: text_request, api_key: str = Depends(verify_api_key)):
     try:
          predictions_raw = text_classifier.predict(texts.texts)
          # Map the keys to match the PredictionResponse schema
          predictions = [
               {"text": item["Text"], "sentiment": item["Sentiment"]}
               for item in predictions_raw
          ]
          return PredictionResponse(predictions=predictions)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e)) 