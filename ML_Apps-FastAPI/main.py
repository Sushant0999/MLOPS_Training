from fastapi import FastAPI

# here object name is app
app = FastAPI()


# object_name.get
@app.get("/")
async def root():
    return {"message": "Hey Viking"}


# object_name.post
@app.post("/post")
async def hello():
    return {"message": "viking"}
