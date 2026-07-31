from pydantic import BaseModel
from typing import Optional, Dict, Any


class WazuhAlert(BaseModel):
    source: str
    timestamp: str
    host: str
    rule_id: str
    severity: int
    group: Optional[str] = None
    summary: str
    details: Optional[Dict[str, Any]] = None
