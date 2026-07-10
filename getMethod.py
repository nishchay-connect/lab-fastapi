from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI()

## now to undertand better from here onwards we will start working on a simple project 
# patient record handling

def load_data():
    with open('patients.json','r') as f:
        data=json.loads(f.read())
    return data

@app.get('/')
def Hello():
    return {'message':'Welcome to patient data management'}

@app.get('/about')
def about():
    return {'message':'This is the software to manage patients data.'}
    
@app.get('/view')
def view():
    return load_data()

@app.get('/view/me')  # we can create endpoints like this as well 
def me():
    return {'message':'you r right '}


@app.get('/view/sort')
# @app.get('/sort')
def sorted_view(sort_by:str=Query(...,description='GIVE THE PARAMETER TO SORT BY'),
                order:str=Query('asc',description='GIVE THE ORDER AS ASC OR DESC')):
    
    parameters=['height_cm','age','weight_kg']

    if sort_by not in parameters:
        raise HTTPException(status_code=400,detail='UNAVAILABLE SERVICE DEMANDED')
    # 400: bad req
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='UNAVAILABLE SERVICE DEMANDED')  
    
    sort_rev=False if order=='asc' else True 
    sorted_data=sorted(load_data().values(),key=lambda x:x.get(sort_by),reverse=sort_rev)

    return sorted_data

#using dynamic after 
@app.get('/view/{patient_id}')
                                    #Path(...,) means a req parameter
def patient_retrieval(patient_id: str=Path(...,description='ID OF PATIENT',examples=['P001'])):
    if patient_id in load_data():
        return load_data()[patient_id]
    else:
        # return {'error':'patient not found'}

        # just to ensure that error is not represented as success
        raise HTTPException(status_code=404,detail='Patient id not found') 