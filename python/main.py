from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI instance
app = FastAPI(
    title="tauri-python-template",
    description="FastAPI template for Tauri apps",
    version="0.1.0",
)

PORT_API = 8008

# Configure CORS settings
origins = [
    "*",  # to whitelist any url, REMOVE THIS FOR PRODUCTION!!!
    # "http://localhost:3000", # for dev
    # "https://your-web-ui.com", # for prod
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/shutdown")
def app_shutdown():
    import os
    import signal

    os.kill(os.getpid(), signal.SIGTERM)


if __name__ == "__main__":
    import uvicorn

    print(f"Starting FastAPI server in http://localhost:{PORT_API}/docs")
    uvicorn.run(app, host="0.0.0.0", port=PORT_API)
