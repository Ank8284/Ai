import os
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv
import ssl
import certifi

# Load environment variables securely
load_dotenv()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    raise RuntimeError("AIPROXY_TOKEN environment variable is not set.")

AI_PROXY_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def get_proxy_headers():
    """Retrieve the authorization headers securely."""
    return {"Authorization": f"Bearer {AIPROXY_TOKEN}", "Content-Type": "application/json"}

@app.post("/chat")
async def chat(request: ChatRequest):
    """Send a message to ProxyAI and return the response."""
    data = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": request.message}]}
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    
    async with httpx.AsyncClient(verify=ssl_context) as client:
        response = await client.post(AI_PROXY_URL, headers=get_proxy_headers(), json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
        return response.json()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Handle file uploads and save them locally."""
    file_location = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename, "message": "File uploaded successfully!"}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
