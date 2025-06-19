from transformers import pipeline

def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")
