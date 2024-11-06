from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
async def root():
    ip = socket.gethostbyname(socket.getfqdn())
    return ip