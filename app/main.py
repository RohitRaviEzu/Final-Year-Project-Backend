from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import admin_routes, camera_routes, detection_logs_routes
from fastapi.responses import FileResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:1234"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(admin_routes.router, prefix="/api")
app.include_router(camera_routes.router, prefix="/api")
app.include_router(detection_logs_routes.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Welcome to Helmet and Safety Vest Detection API"}

# # Serve the favicon
# @app.get("/favicon.ico", include_in_schema=False)
# async def favicon():
#     return FileResponse("app/static/favicon.ico")

# uvicorn app.main:app --reload
