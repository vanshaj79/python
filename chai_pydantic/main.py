from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


def main():
    print("Hello from chai-pydantic")
    uvicorn.run(app, host="0.0.0", port=8000)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    main()
