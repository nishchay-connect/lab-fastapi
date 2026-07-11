# FastAPI
Finally exploring the Serving/Deployment side.
# METHODS
- GET
- POST
- PUT
- DELETE

# NOTES
The realisation is that the routes are checked in regitration order i.e its adviced to have static endpoints defined first and then the dynamic ones.

The syntax error in json can (file or dataset) can give a server error 500 internal error
(bool in json is true not True)

Simply just creating a file(say App.py) with app empty object and then seperate files(Say getMethod) importing that object and making end points ,nd then importing the (App.py) in main and executing it doenst creates endpoints as files(getMethod) never got executed so such imports way doesnt works ,so how do we solve this as project grows??
 
Now Comes
# Routers
instead of @app.get we do @router.get()

where router is router=APIRouter()
 
and how it is used is 

from file import router as r1
app=FastAPI()
app.include_router(r1)


