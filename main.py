from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Hola desde FastAPI en Azure"}

@app.get("/saludo")
def saludo():
    return {"mensaje": "Bienvenido Manuel"}
