from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from Schema.Userinput import UserInput
from Schema.PredResponse import Response
from model.predict import predict_ouput,MODEL_VERSION,model

app=FastAPI()
@app.get('/')
def home():
    return {'message':'Welcome To INSURANCE Premium Prediction'}

# things req to make it machine readable
@app.get('/health') ## its mainly added because its common defined when we deploy on cloud
def health_check():
    return {'status':'ok','version':MODEL_VERSION,'model_loaded':model is not None}

@app.post('/predict',response_model=Response)
def predict_premium(userInput:UserInput):
    
    pyd_dict=userInput.model_dump()
    out={} # the req attributes for model
    for k,v in pyd_dict.items():
        if k in ['bmi','age_group','lifestyle_risk','city_tier','income_lpa','occupation']:
            out[k]=v
    try:
        prediction=predict_ouput(out)
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    
    return JSONResponse(status_code=200,content={'response':{'prediction':prediction}})


