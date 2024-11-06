from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root(request: Request):
    ip = request.client.host
    return ip