from transformers import pipeline

class EmpathyResponse:
    def __init__(self):
        self.model_pipeline = pipeline("text2text-generation", model = "benjaminbeilharz/dialoGPT-small-empatheticdialogues-generation")
    
    def predict(self, query):
        return self.model_pipeline(query)
