from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import base64
import io
import os
import pandas as pd

from agent import process_query

# Load dataset here also for visualization
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "titanic.csv"))

app = FastAPI()

class Query(BaseModel):
    question: str


@app.post("/ask")
def ask(query: Query):
    result = process_query(query.question)

    if result == "VISUALIZE_AGE_HISTOGRAM":
        plt.figure()
        df["age"].dropna().hist(bins=20)
        plt.title("Age Distribution of Titanic Passengers")

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        plt.close()
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()

        return JSONResponse(
            content={
                "answer": "Here is the age distribution histogram.",
                "image": image_base64
            }
        )

    return {"answer": result}