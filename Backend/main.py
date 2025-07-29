from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import schemas, model, feature_extraction
from fastapi.responses import JSONResponse
import joblib
from collections import Counter

app = FastAPI(title='Phising API', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_headers = ['*'],
    allow_methods = ['*'],
    allow_credentials = True,
    allow_origins = ['*']
)

models = {
    "Random Forest": joblib.load("model/random_forest_model.pkl"),
    "Naive Bayes": joblib.load("model/naive_bayes_model.pkl"),
    "SVM": joblib.load("model/svm_model.pkl")
}

@app.get("/")
def root():
    return {"message": "Phishing API"}

@app.post('/predict', status_code=201)
async def predict(data:schemas.PhishingFeatures):
    try:
        features = feature_extraction.features(data.url)
    except Exception as e:
        raise HTTPException(status_code=404, detail=(str(e)))
    results = {}
    
    preds = [model.predict([features])[0] for model in models.values()]
    final_pred = Counter(preds).most_common(1)[0][0]
    results = final_pred
    return {
        "url": data.url,
        "predictions": results

    }
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=3214, reload=True)