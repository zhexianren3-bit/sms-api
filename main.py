from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "短信API"}
@app.post("/send")
def send(phone: str, code: str):
    return {"success": True, "msg": "发送成功"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
