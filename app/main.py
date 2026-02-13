from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.reviewer import review_code

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/review")
async def review(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode("utf-8", errors="ignore")

    if len(decoded) > 8000:
        return {"review": "File too large. Please upload a smaller file."}

    try:
        result = review_code(decoded)
        return {"review": result}
    except Exception as e:
        return {"review": f"Server Error: {str(e)}"}
