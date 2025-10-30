from pydantic import BaseModel, Field
from typing import List



class text_request(BaseModel):
     texts: List[str] = Field(..., description="List of texts to analyze them", min_length=1)
     
     '''
     Schema Example
     '''
     class Config:
          json_schema_extra = {
               "example": {
                    "texts": [
                         "This is a text",
                         "This is another text"
                    ]
               }
          }
          

class SentimentPrediction(BaseModel):
     text: str = Field(..., description="Text to analyze")
     sentiment: str = Field(..., description="Sentiment of the text")
     
     '''
     Schema Example
     '''
     class Config:
          json_schema_extra = {
               "example": {
                    "text": "This is a text",
                    "sentiment": "positive"
               }
          }
          
          
class PredictionResponse(BaseModel):
     predictions: List[SentimentPrediction] = Field(..., description="List of predictions")

     '''
     Schema Example
     '''
     class Config:
          json_schema_extra = {
               "example": {
                    "predictions": [
                         {
                              "text": "This is a text",
                              "sentiment": "positive"
                         },
                         {
                              "text": "This is another text",
                              "sentiment": "negative"
                         }
                    ]
               }
          }