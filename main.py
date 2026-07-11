# import getMethod
# app=getMethod.app

# import postMethod
# app=postMethod.app

## even better aproach
# from fastapi import FastAPI  # doesnt works due to circular imports
# app=FastAPI()

# from App import app
# app=app

from putDelMethod import app
app=app