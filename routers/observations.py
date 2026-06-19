from fastapi import APIRouter

from schemas.observation_schema import (
    ObservationCreate,
    ObservationResponse
)

from services.database_service import (
    save_observation,
    save_alert
)

from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

router = APIRouter()


@router.post(
    "/",
    response_model=ObservationResponse
)
def create_observation(
    observation: ObservationCreate
):

    # Save observation
    save_observation(
        observation.model_dump()
    )

    # Create alert if risk is High or Critical
    if observation.risk_level in [
        "High",
        "Critical"
    ]:

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
            "risk_level": observation.risk_level,
            "deterrence_action": observation.deterrence_action,
            "status": "Active"
        }

        save_alert(alert_data)

    return observation