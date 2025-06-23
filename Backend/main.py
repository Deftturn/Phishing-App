from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import schemas, model, feature_extraction

app = FastAPI(title='Phising API', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_headers = ['*'],
    allow_methods = ['*'],
    allow_credentials = True,
    allow_origins = ['*']
)

@app.get("/")
def root():
    return {"message": "Phishing API"}

@app.post('/predict')
async def predict(data:schemas.PhishingFeatures):
    fturs = feature_extraction.features(data.url)
    prediction = model.predict(fturs)
    label = "Phishing" if prediction == -1 else "Legitimate"
    return {"prediction":label}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=3214, reload=True)