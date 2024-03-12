from fastapi import FastAPI

app = FastAPI()


@app.get("/serv")
def read_root():
    return {"Hello": "World"}

# uvicorn serv:app --reload --port 8000
