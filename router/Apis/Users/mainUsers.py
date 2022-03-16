import sys
sys.path.append("../../../")

from fastapi 				import APIRouter
from fastapi.params			import Depends
from sqlalchemy				import schema
from sqlalchemy.orm.session	import Session
from sqlalchemy.future		import select
from providers.connection	import SeccionLocal
from typing 				import List
import asyncio
import providers.UserSchema
from  models.User 			import User 

routerUser = APIRouter(prefix="/api/users")



async def get_db():
	try:
		seccion = SeccionLocal()
		yield seccion
	finally:
		pass

def getusers(session):
	return session.query(User).all()

@routerUser.get("/fetchall-users", response_model=List[providers.UserSchema.UserGet]) 
async def fetchall_users(db: Session= Depends(get_db)):
	users = await db.run_sync(getusers)
	print('ACA:  FETCH -->',users)
	return users
@routerUser.post("/create-users", response_model= providers.UserSchema.User)
async def create_users(req:providers.UserSchema.User, db:Session = Depends(get_db)):
	user = User(
				name		=  	req.name,
				username	= 	req.username ,
				password	= 	req.password
			)
	db.add(user)
	await db.commit()
	await db.refresh(user)
	return user