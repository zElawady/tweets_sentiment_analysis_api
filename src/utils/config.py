import os
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import joblib
import gensim.downloader as api



# Load environment variables from .env file
load_dotenv()

# Class Validation
# This class is used to load environment variables from a .env file
class Settings(BaseSettings):
    APP_NAME: str = "Sentiment Analysis API"
    VERSION: str = "1.0.0"
    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "your-default-secret-key")
    MODEL_PATH: str = "Artifacts"
    PORT: int = 5000
    HOST: str = "127.0.0.1"



# Create a function to load the settings
# This function will be used to load the settings from the .env file
@lru_cache() # Least Recently Used Cache will always get the same instance without the overhead of creating a new Settings object each time.
def get_settings() -> Settings:
    return Settings()




# Create variable to access the artifacts dir
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTIFACTS_DIR = os.path.join(PROJECT_DIR, "Artifacts")


# Load vectorizers
tfidf_vectorizer = joblib.load(os.path.join(ARTIFACTS_DIR, "tf-idf.pkl"))
bow_vectorizer = joblib.load(os.path.join(ARTIFACTS_DIR, "bow.pkl"))
glove_vectorizer = api.load("glove-twitter-25")

# Load models
svm_ifidf_model = joblib.load(os.path.join(ARTIFACTS_DIR, "svm_model_tfidf.pkl"))
svm_bow_model = joblib.load(os.path.join(ARTIFACTS_DIR, "svm_model_bow.pkl"))
svm_glove_model = joblib.load(os.path.join(ARTIFACTS_DIR, "svm_model_glove.pkl"))
rf_ifidf_model = joblib.load(os.path.join(ARTIFACTS_DIR, "rf_model_tfidf.pkl"))
rf_bow_model = joblib.load(os.path.join(ARTIFACTS_DIR, "rf_model_bow.pkl"))
rf_glove_model = joblib.load(os.path.join(ARTIFACTS_DIR, "rf_model_glove.pkl"))



# Create a dictionary for emojis maps
EMOTIONS_DICT = {
    # 🙂 Emojis
    "😀": "grinning face",
    "😁": "beaming face with smiling eyes",
    "😂": "face with tears of joy",
    "🤣": "rolling on the floor laughing",
    "😃": "grinning face with big eyes",
    "😄": "grinning face with smiling eyes",
    "😅": "grinning face with sweat",
    "😉": "winking face",
    "😊": "smiling face with smiling eyes",
    "😍": "smiling face with heart eyes",
    "😘": "face blowing a kiss",
    "😎": "smiling face with sunglasses",
    "🥰": "smiling face with hearts",
    "😒": "unamused face",
    "😭": "loudly crying face",
    "😢": "crying face",
    "😡": "angry face",
    "😠": "angry face",
    "🤬": "face with symbols on mouth",
    "😩": "weary face",
    "😤": "face with steam from nose",
    "🤯": "exploding head",
    "😱": "screaming in fear",
    "👍": "thumbs up",
    "👎": "thumbs down",
    "❤️": "love",
    "💔": "broken heart",
    "🔥": "fire",
    "💯": "hundred points",
    "🙏": "folded hands",

    # 🙂 Emoticons
    ":)": "smiley face",
    ":-)": "smiley face",
    ":D": "grinning face",
    ":-D": "grinning face",
    ":(": "sad face",
    ":-(": "sad face",
    ":/": "unsure face",
    ":-/": "unsure face",
    ":|": "neutral face",
    ":-|": "neutral face",
    ":'(": "crying face",
    ":'-)": "crying face",
    ":P": "playful face",
    ":-P": "playful face",
    ";)": "winking face",
    ";-)": "winking face",
    ">:(": "angry face",
    "<3": "love",
    "</3": "broken heart"
}


# Neccessary stop words for text processing
NEGATION_STOPWORDS = [
    "no", "not", "nor", "never", "n't", "cannot",
    "don't", "doesn't", "didn't", "won't", "wouldn't",
    "shouldn't", "can't", "couldn't", "isn't", "aren't", 
    "wasn't", "weren't", "nothing", "nowhere", "neither", "nobody", "none"]


# Create a dictionary for class maps
CLASS_MAPS = {
    0: "Negative",
    1: "Positive",
    2: "Neutral"
}