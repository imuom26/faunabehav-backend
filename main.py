from fastapi import FastAPI
from routers.events import router as events_router
from routers.observations import router as observations_router
from routers.alerts import router as alerts_router
from routers.devices import router as devices_router
from routers.feedback import router as feedback_router
from routers.dashboard import router as dashboard_router

app = FastAPI()

app.include_router(
    events_router,
    prefix="/events",
    tags=["Events"]
)
app.include_router(
    observations_router,
    prefix="/observations",
    tags=["Observations"]
)
app.include_router(
    alerts_router,
    prefix="/alerts",
    tags=["Alerts"]
)
app.include_router(
    devices_router,
    prefix="/devices",
    tags=["Devices"]
)
app.include_router(
    feedback_router,
    prefix="/feedback",
    tags=["Feedback"]
)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "FaunaBehav Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}