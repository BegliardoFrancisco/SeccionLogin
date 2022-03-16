from fastapi				import FastAPI
from fastapi.params			import Depends
from starlette.responses	import RedirectResponse
from models.User			import main
from router.Apis.Users 		import mainUsers			
import asyncio 



app = FastAPI()


app.include_router(mainUsers.routerUser)
