from fastapi import FastAPI

app = FastAPI(title="OSINT-Plattform")


@app.get("/health")
def health():
    return {"status": "ok"}
