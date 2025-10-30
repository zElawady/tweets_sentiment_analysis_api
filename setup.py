from setuptools import setup, find_packages

setup(
    name="sentiment-analysis-api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.115.6",
        "uvicorn==0.34.0",
        "streamlit==1.44.1",
        "pydantic==2.10.5",
        "scikit-learn==1.6.0",
        "joblib==1.4.2",
        "python-dotenv==1.0.1",
        "python-multipart==0.0.20",
        "imbalanced-learn==0.13.0",
        "wordcloud==1.9.4",
        "gensim==4.3.3",
        "spacy==3.8.4",
        "nltk==3.6.5",
        "pydantic-settings==2.2.1"
    ],
) 