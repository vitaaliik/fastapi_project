from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello bro"}

@app.get("/test")
def read_test():
    return {"status": "test branch works"}