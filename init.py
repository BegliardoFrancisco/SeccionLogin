from fastapi import FastAPI





app = FastAPI()


@app.get('/')
async def main(req):
	return f"Hellow Word {req}"

app.run()