from fastapi import FastAPI
from pydantic import BaseModel
from app.ml.neural_model import train_neural_model, predict_weak_area
from app.ml.symbolic_engine import get_learning_advice

app = FastAPI()
model = train_neural_model()

class Student(BaseModel):
    name: str
    html: int
    css: int
    js: int
    confidence: str

@app.post("/predict")
def predict(student: Student):
    weak = predict_weak_area(model, student.html, student.css, student.js)
    feedback = get_learning_advice(weak, student.confidence)
    return {
        "name": student.name,
        "weak_area": weak.replace("_score", "").upper(),
        "advice": feedback
    }
