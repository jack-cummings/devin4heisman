import re
import json
import os
import datetime
from fastapi import FastAPI, Request, BackgroundTasks, Response, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import traceback



app = FastAPI()
templates = Jinja2Templates(directory='templates')
#app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})



if __name__ == '__main__':
    if os.environ['MODE'] == 'dev':
        import uvicorn
        uvicorn.run(app, port=4242, host='0.0.0.0')
