from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import re

app = FastAPI(title="AI Energy Analyzer")


class PromptRequest(BaseModel):
    prompt: str


def analyze_prompt(prompt: str):
    words = re.findall(r"\S+", prompt)
    word_count = len(words)
    character_count = len(prompt)

    technical_keywords = [
        "calculate", "derive", "equation", "mathematical",
        "algorithm", "code", "python", "simulation",
        "optimization", "stability", "inverter",
        "power", "system", "analyze", "compare",
        "prove", "physics", "engineering"
    ]

    technical_count = sum(
        1 for word in technical_keywords
        if word in prompt.lower()
    )

    sentences = max(1, len(re.findall(r"[.!?]+", prompt)))

    question_bonus = 4 if "?" in prompt else 0

    workload = (
        15
        + word_count * 1.5
        + character_count / 300
        + technical_count * 6
        + sentences * 2
        + question_bonus
    )

    workload = max(5, min(98, workload))

    input_tokens = max(
        1,
        round(word_count * 1.35)
    )

    output_tokens = round(
        100 + workload * 6
    )

    duration = (
        2.0
        + output_tokens / 180
        + workload / 100
    )

    duration = min(duration, 15)

    if workload < 30:
        complexity = "Low"
    elif workload < 60:
        complexity = "Moderate"
    elif workload < 80:
        complexity = "High"
    else:
        complexity = "Very High"

    return {
        "workload": round(workload),
        "complexity": complexity,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "duration": round(duration, 2),
    }


@app.post("/api/analyze")
def analyze(request: PromptRequest):
    return analyze_prompt(request.prompt)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
def home():
    return FileResponse("static/index.html")