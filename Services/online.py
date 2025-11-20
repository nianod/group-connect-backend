from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class onlineSession(BaseModel):
    sessionTitle: str = Field(..., min_length=5, max_length=100)
    subject: str
    meetingLink: str
    meetingDate: Optional[str] = None
    meetingTime: Optional[str] = None
    duration: str
    description: str
    meetingPlatform: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
