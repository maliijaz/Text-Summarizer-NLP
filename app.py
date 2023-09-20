from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is Text Summarizer"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
      return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
      try:
            os.system("python main.py")
            return Response("Training Completed")
      
      except Exception as e:
            return Response(f"Error occurred{e}")
      

@app.get("/predict")
async def predict(text):
      try:
            obj = PredictionPipeline()
            text = obj.predict(text)
            return text
      
      except Exception as e:
            raise e
      

if __name__ == "__main__":
      uvicorn.run(app, host="0.0.0.0", port=8080)
      