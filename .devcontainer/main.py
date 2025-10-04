from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello():
    return {"ok": True, "msg": "Codespaces + FastAPI running"}
