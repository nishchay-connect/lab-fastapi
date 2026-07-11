import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field, computed_field
from typing import Annotated,Literal
from featureMethods import city_tier,lifestyle_risk,age_group
import pandas as pd
#GET MODEL
with open('model.pkl','rb') as f:
    model=pickle.load(f)

# Making Pydantic Model
class UserInput(BaseModel):
    #age	weight	height	income_lpa	smoker	city	occupation	
    age:Annotated[int,Field(...,gt=0,description='Enter the age of User',examples=[34])]
    weight:Annotated[float,Field(...,gt=0,description='Enter the weight of User',examples=[70])]
    height:Annotated[float,Field(...,gt=0,description='Enter the height of User',examples=[1.7])]
    income_lpa:Annotated[float,Field(...,gt=0,description='Enter the income of User',examples=[12.3])]
    smoker:Annotated[bool,Field(...,description='Enter wether USER smokes or not(True/False)')]
    city:Annotated[str,Field(...,description='Enter the age of User',examples=['Mumbai'])]
    occupation:Annotated[Literal[  'retired','freelancer',  'student', 'government_job',
'business_owner', 'unemployed','private_job'],Field(...,description='Enter the age of User')]
    
    @computed_field
    @property
    def bmi(self) ->float:
        return self.weight/self.height**2
    
    @computed_field
    @property
    def age_group(self) ->str:
       return age_group(self.age)
    
    @computed_field
    @property
    def lifestyle_risk(self) ->str:
       return lifestyle_risk(self.smoker,self.bmi)
        
    @computed_field
    @property
    def city_tier(self) ->int:
        return city_tier(self.city)

app=FastAPI()
@app.post('/predict')
def predict_premium(userInput:UserInput):
    pyd_dict=userInput.model_dump()
    out={} # the req attributes for model
    for k,v in pyd_dict.items():
        if k in ['bmi','age_group','lifestyle_risk','city_tier','income_lpa','occupation']:
            out[k]=v
## was giving some error (yet it was working though but code editor was marking it )
    # input_df=pd.DataFrame(
    #     [userInput.model_dump(include=['bmi','age_group','lifestyle_risk','city_tier','income_lpa','occupation'])])


    input_df=pd.DataFrame([out])
    prediction=model.predict(input_df)[0]
    prediction=model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={'response':{'predicted_category':prediction}})


