from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

class PredictionInput(BaseModel):
    age: int
    study_hours: float
    class_attendance: float
    sleep_hours: float

@app.post('/predict_model')
def predict_model(Input_data: PredictionInput):

    new_data = pd.DataFrame({
        'age': Input_data.age,
        'study_hours': Input_data.study_hours,
        'class_attendance': Input_data.class_attendance,
        'sleep_hours': Input_data.sleep_hours,
    })

    predictions = model.predict(new_data)

    return {'prediction': predictions}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = '0.0.0.0', port = 5000)