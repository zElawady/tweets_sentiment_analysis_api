import numpy as np

from typing import List, Dict

from .text_processor import TextProcessor
from .config import (tfidf_vectorizer, 
                        bow_vectorizer,
                        glove_vectorizer)

from .config import (svm_ifidf_model,
                        svm_bow_model,
                        svm_glove_model,
                        rf_ifidf_model,
                        rf_bow_model,
                        rf_glove_model)

from .config import CLASS_MAPS


class TextClassifier:
     def __init__(self, model_type: str = "   Glove   ", model_name: str = "svm"):
          self.processor = TextProcessor()
          self.class_maps = CLASS_MAPS
          self.model = None
          self.vectorizer = None
          self.model_type = model_type.lower().strip()
          self.model_name = model_name.lower().strip()
          
          if model_type == "tfidf":
               self.vectorizer = tfidf_vectorizer
               if model_name == "svm":
                    self.model = svm_ifidf_model
               elif model_name == "rf":
                    self.model = rf_ifidf_model
               else:
                    raise ValueError("Invalid model name. Choose 'svm' or 'rf'.")
               
               
          elif model_type == "bow":
               self.vectorizer = bow_vectorizer
               if model_name == "svm":
                    self.model = svm_bow_model
               elif model_name == "rf":
                    self.model = rf_bow_model
               else:
                    raise ValueError("Invalid model name. Choose 'svm' or 'rf'.")
               
          elif model_type == "glove":
               self.vectorizer = glove_vectorizer
               if model_name == "svm":
                    self.model = svm_glove_model
               elif model_name == "rf":
                    self.model = rf_glove_model
               else:
                    raise ValueError("Invalid model name. Choose 'svm' or 'rf'.")
               
          else:     
               raise ValueError("Invalid model type. Choose 'tfidf' or 'bow' or 'glove'")
          
          
     def predict(self, texts: List[str]) -> List[Dict[str, str]]:
          # Text Preprocessing
          proccessed_texts = [self.processor.process_text(text) for text in texts]
          
          # Vectorization
          if self.model_type == "glove":
               vectorized_texts = []
               for text in proccessed_texts:
                    words = text.split()
                    vector_words = [self.vectorizer[word] for word in words if word in self.vectorizer]
                    if len(vector_words) == 0:
                         vectorized_texts.append(np.zeros(self.vectorizer.vector_size))
                    else:
                         vectorized_texts.append(np.mean(vector_words, axis=0))
               vectorized_texts = np.array(vectorized_texts)
               
          else:  
               vectorized_texts = self.vectorizer.transform(proccessed_texts).toarray()
          
          # Prediction
          raw_predictions = self.model.predict(vectorized_texts)
          
          predictions = []
          
          for text, pred in zip(texts, raw_predictions):
               pred_label = self.class_maps.get(int(pred), "Unknown")
               predictions.append({"Text": text, "Sentiment": pred_label})
               
          return predictions



