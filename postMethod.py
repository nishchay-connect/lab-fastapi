from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from matplotlib.patheffects import PathEffectRenderer
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json
# from getMethod import app  # this works as well 

def load_data():
    with open('patients.json','r') as f:
        data=json.loads(f.read())
    return data

def save_data(data:dict):
    with open('patients.json','w') as f:
        json.dump(data,f,indent=2)

# as moving ahead with our sample project now we will create endpoint to create new patient

## CREATING OUR PYDANTIC MODEL
class Patient(BaseModel):

# we realise here that we r writing a lot of code here but its actually req for the user at client to use API
    id:Annotated[str,Field(...,description='ID OF PATIENT',examples=['P001'])]
    name:Annotated[str,Field(...,description='NAME OF PATIENT',examples=['Rohit'])]
    city:Annotated[str,Field(...,description='CITY OF PATIENT',examples=['Delhi'])]
    age:Annotated[int,Field(...,description='AGE OF PATIENT',examples=[32,43],gt=0,lt=120)]
    gender:Annotated[Literal['male','female','others'],Field(...,description='GENDER OF PATIENT',examples=['male'])]
    height:Annotated[float,Field(...,description='HEIGHT OF PATIENT (m)',examples=[1.7])]
    weight:Annotated[float,Field(...,description='WEIGHT OF PATIENT',examples=[67.2])]

    @computed_field
    @property 
    def bmi(self) -> float:
        bmi=round(self.weight/self.height**2,2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) ->str:
        if self.bmi<18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi<30:
            return 'Normal'
        else:
            return 'Obese'

app=FastAPI()

@app.post('/create')
def add_patient(patient:Patient): # the func name reflects in docs as well 

    data=load_data()

    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient ALREADY EXISTS')
    
    data[patient.id]=patient.model_dump(exclude=["id"])

    save_data(data)

    return JSONResponse(status_code=201,content={'message':f"Patient with id {patient.id} created successfully..."})


