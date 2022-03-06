import sys 
sys.path.append("../providers")

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from connection import Base, engine


class User(Base): 
	__tablename__= "users"
	id 			= Column(Integer, primary_key=True, index=True)
	email		= Column(String(255), index=True)
	password	= Column(String(255))
	

async def main():

	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)

	await engine.dispose()

