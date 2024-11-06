from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root(request: Request):
    ip = request.client.host
    ret = f"Your IP: {ip}"
    return ret