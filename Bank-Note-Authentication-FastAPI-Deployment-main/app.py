from fastapi import FastAPI
from BankNotes import NoteParam
import uvicorn
import pickle


app = FastAPI()

pickle_in = open('BankNotes/classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.get('/')
def home():
    return {'Message': 'Hello Stranger'}


@app.get('/Welcome/{name}')
def welcome(name: str):
    return {'Message': f'Hello {name}'}


@app.post('/predict')
def predict_banknote(data: NoteParam):
    data = data.dict()
    
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]
    
    score = classifier.predict([[variance, skewness, curtosis, entropy]])
    if score[0] > 0.5:
        prediction = 'Fake Note'
    else:
        prediction = 'Bank Note'
                
    return {'Prediction': prediction}
    


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)