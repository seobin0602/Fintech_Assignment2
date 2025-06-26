from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class LoanApplication(BaseModel):
    name: str
    business_type: str
    monthly_income: float
    requested_amount: float
    country: str
    national_id: str
## KYC checks endpoint
@app.post("/score")
def score_app(app: LoanApplication):
    if not app.national_id.startswith("ID"):
        return {"error": "KYC failed: Invalid national ID format."}
    score = min(100, int(app.monthly_income / app.requested_amount * 40) + random.randint(0, 10))
    approved = score >= 60
    return {"credit_score": score, "approved": approved, "kyc_passed": True}
## timestamp
@app.post("/pay")
def simulate_payment():
    return {
        "status": "success",
        "tx_hash": "0xabc123fakehash789",
        "timestamp": "2025-06-19T12:34:56Z",
        "fee_usd": 0.02,
        "network": "Polygon",
        "token": "USDC"
    }
