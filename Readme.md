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

# WHAT METHOD TO CHOOSE WHEN
- one important note down is that actually at a fundamental level get or post or any method isnt different but actually its the intentionally designed convention to seperate the type of request
s
- on the level of client server interaction its not diff as much but how is it interpreted and worked with is different so that everyone can work with it and theirs a uniformity and ease in the web development arena

- get is expected to be that it wont do any change on server ,post is expected to provide data ,to work with on the server (which doesnt mean u cant do processing with get req but as we mentioned its a accepted defined convention)
{that get is idempotent and post is not}

# Linking to frontend
and finally what the motive of API development is ,reached to serving the API to frontend 

something like this using streamlit

-    response = requests.post(API_URL, json=input_data)

and as we go towards development ,production side your frontends become much more that a .py but actually folders having html ,css,js or modern frameworks files.


