from fastapi import FastAPI
import pymyip

app = FastAPI()

@app.get("/")
async def root():
    ip = pymyip.get_ip()
    return ip