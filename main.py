from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    rand = random.randint(1,99)
    txt = f"Випадковe число від 1 до 99: {rand}"
    return txt