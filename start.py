from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def Hello():
    return {'message':'hello world'}

@app.get('/about')
def about():
    return {'message':'hey welcome to the world'}