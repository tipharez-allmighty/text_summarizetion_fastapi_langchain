from fastapi import FastAPI
import uvicorn
from summarizer import SimpleSummarizer
from pydantic import BaseModel

app = FastAPI()


class SummarizerPayload(BaseModel):
    text: str


@app.post("/summarize")
async def summarize(summ_payload: SummarizerPayload):
    """
    Endpoint to receive text input and return a summarized version using SimpleSummarizer.

    Args:
    - summ_payload (SummarizerPayload): Input data containing text to be summarized.

    Returns:
    - dict: A JSON object containing the summarized text under the key "summary".
    """

    summarizer = SimpleSummarizer()
    summary = summarizer.summarizer(summ_payload.text)
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
