from fastapi import FastAPI

app = FastAPI(title="Documentation API")

@app.get("/")
async def root():
    return {"message": "Hello World"}