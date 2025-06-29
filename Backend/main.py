from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import schemas, model, feature_extraction
from fastapi.responses import JSONResponse

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

@app.post('/predict', status_code=201)
async def predict(data:schemas.PhishingFeatures):
    fturs = feature_extraction.features(data.url)
    prediction = model.predict(fturs)
    # label = "A Phishing URL" if prediction == -1 else "A Legitimate URL"
    return JSONResponse(content={"prediction":prediction})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=3214, reload=True)