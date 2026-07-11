from pydantic import BaseModel,Field
from typing import Dict,Annotated

class Response(BaseModel):

    predicted_category:Annotated[str,Field(...,description='Predicted Class')]
    confidence:Annotated[float,Field(...,description='Confidence of Predicted class')]
    class_probabilities:Annotated[Dict[str,float],Field(...,description='Probabilities of all classes')]