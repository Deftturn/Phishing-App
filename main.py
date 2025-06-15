from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=3214)