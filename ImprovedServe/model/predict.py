from multiprocessing import process

import pandas as pd
import pickle

MODEL_VERSION='1.0.0' # usually done using mlflow tool 

#GET MODEL
with open('model/model.pkl','rb') as f:
    model=pickle.load(f)

class_labels=model.classes_.tolist()

def predict_ouput(userInput:dict):
    input_df=pd.DataFrame([userInput])
    predicted_class=model.predict(input_df)[0]

    probs=model.predict_proba(input_df)[0]

    conf=max(probs)

    class_probs=dict(zip(class_labels,map(lambda x:round(x,4),probs)))


    return {'predicted_category':predicted_class,
            "confidence":conf,
            'class_probabilities':class_probs}
