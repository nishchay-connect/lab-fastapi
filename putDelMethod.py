
from json import load

from fastapi import FastAPI,HTTPException
from typing import Literal, Optional,Annotated
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sympy import det
from postMethod import load_data,save_data,Patient
# we dont use the existing patient class becuase it had all req fields but in update we dont know
# what would come

class PatientUpdate(BaseModel):
    
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None,gt=0)]
    gender:Annotated[Optional[Literal['male','female']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]


app=FastAPI()

@app.put('/update/{patient_id}')
def update_data(patient_id:str,patient_update:PatientUpdate):

    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient ID not found...')

    updated_patient_info=patient_update.model_dump(exclude_unset=True)

    patient_existing_data=data[patient_id]

    for key,val in updated_patient_info.items():
        patient_existing_data[key]=val

    # now we need to save this data but , computed fields req to be recalculated
    patient_existing_data['id']=patient_id
    patient_=Patient(**patient_existing_data)
    data[patient_id]=patient_.model_dump(exclude=['id'])

    save_data(data)
    return JSONResponse(status_code=200,content='Patient Updated')

## these all can be done in more efficient way probably designing Flags in the base class
# as update=true/false, so that no more classes are req to create, also various other design changes
# can be done

## DEL METHOD
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient Id does not exists')
    
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content={"message":f'Patient with id {patient_id} deleted....'})

    

