from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import matplotlib.pyplot as plt
import base64
import io
import pandas as pd

from agent import process_query

# Load dataset here also for visualization
df = pd.read_csv("titanic.csv")

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
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()

        return JSONResponse(
            content={
                "answer": "Here is the age distribution histogram.",
                "image": image_base64
            }
        )

    return {"answer": result}