from typing 	import Optional, List
from pydantic 	import EmailStr, BaseModel


class User(BaseModel):
	id:			Optional[int]
	name:		str
	username:	str
	password: 	str
	
	class Config:
		orm_mode=	True

class UserUpdate(BaseModel):
	name:	 	str
	username:	str
	password:	str


class UserGet(BaseModel):
	name:str
	username:str
	class Config():
		orm_mode = True

class Response(BaseModel):
	mensaje: str
