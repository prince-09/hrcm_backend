from fastapi import FastAPI
from app.endpoints import claims, payments, adjustments, analytics
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="Healthcare RCM Backend")

origins = [
    "http://localhost:3000",  # For development, Next.js frontend
    "https://yourfrontenddomain.com",  # Add your production frontend domain here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow frontend domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(claims.router, prefix="/claims", tags=["Claims"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(adjustments.router, prefix="/adjustments", tags=["Adjustments"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
async def root():
    return {"message": "Healthcare RCM API is running!"}
