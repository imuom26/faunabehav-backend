from pydantic import BaseModel


class InferenceRequest(BaseModel):
    device_id: int
    frame_path: str

    animal: str
    behaviour: str
    confidence: float


class InferenceResponse(BaseModel):
    animal: str
    behaviour: str
    confidence: float
    risk_level: str
    deterrence_action: str