from fastapi import APIRouter

from schemas.event_schema import (
    InferenceRequest,
    InferenceResponse
)

from services.inference_service import process_inference
from supabase import create_client
from dotenv import load_dotenv
import os
from services.database_service import (
    save_observation,
    save_alert
)

router = APIRouter()

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


@router.get("/")
def get_events():

    response = (
        supabase
        .table("events")
        .select("*")
        .order("event_id", desc=True)
        .execute()
    )

    return response.data

@router.post(
    "/inference",
    response_model=InferenceResponse
)
def run_inference(
    request: InferenceRequest
):

    result = process_inference(
        animal=request.animal,
        behaviour=request.behaviour,
        confidence=request.confidence
    )

    event_data = {
        "device_id": request.device_id,
        "animal": result["animal"],
        "behaviour": result["behaviour"],
        "confidence": result["confidence"],
        "risk_level": result["risk_level"],
        "deterrence_action": result["deterrence_action"],
        "frame_path": request.frame_path
    }

    save_observation(event_data)

    if result["risk_level"] == "High":

        latest_event = (
            supabase
            .table("events")
            .select("event_id")
            .order("event_id", desc=True)
            .limit(1)
            .execute()
        )

        event_id = latest_event.data[0]["event_id"]

        alert_data = {
            "event_id": event_id,
            "status": "Active",
            "deterrence_action": result["deterrence_action"],
            "acknowledged_by": None,
            "risk_level": result["risk_level"]
        }

        save_alert(alert_data)

    return result