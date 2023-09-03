from os import getenv
from dotenv import load_dotenv

load_dotenv()

import uvicorn
from app import app


if __name__ == "__main__":
    uvicorn.run(app, host=getenv("app.host"), port=getenv("app.port"))
