from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

request_count = 0

class PredictionInput(BaseModel):
    age: int
    gender: str
    course: str
    study_hours: float
    class_attendance: float
    internet_access: bool
    sleep_hours: float
    sleep_quality: str
    study_method: str
    facility_rating: str
    exam_difficulty: str

@app.get('/stats')
def stats():
    return {'request count': request_count}

@app.get('/health')
def health():
    return {'status': 'OK'}

@app.post('/predict_model')
def predict_model(Input_data: PredictionInput):
    global request_count
    request_count += 1

    new_data = pd.DataFrame({
        'age': Input_data.age,
        'gender': Input_data.gender,
        'course': Input_data.course,
        'study_hours': Input_data.study_hours,
        'class_attendance': Input_data.class_attendance,
        'internet_access': Input_data.internet_access,
        'sleep_hours': Input_data.sleep_hours,
        'sleep_quality': Input_data.sleep_quality,
        'study_method': Input_data.study_method,
        'facility_rating': Input_data.facility_rating,
        'exam_difficulty': Input_data.exam_difficulty
    })

    predictions = model.predict(new_data)

    return {'prediction': predictions}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = '0.0.0.0', port = 5000)