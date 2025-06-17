from pydantic import BaseModel
from typing import List

class PhishingFeatures(BaseModel):
    features: List[float]