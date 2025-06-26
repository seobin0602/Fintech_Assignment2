# SMEily_MVP ReadMe

# SMEily 💸

SMEily is a global lending and payments platform designed for underserved SMEs around the world. The MVP connects borrowers and investors using blockchain, stablecoins, and real-time credit scoring — offering a fully automated, transparent, and borderless lending experience.

---

## 🚀 MVP Summary

In this stage, SMEily supports:

- Digital loan application via a Streamlit interface
- Real-time credit scoring based on financial input
- Mock KYC/AML verification logic
- Simulated USDC payment and smart contract behavior
- Transparent feedback and approval decision logic

---

## ⚙️ Tech Stack

| Layer       | Technology             |
|------------|------------------------|
| Language    | Python 3.9+            |
| Backend     | FastAPI (REST API)     |
| Frontend    | Streamlit              |
| Deployment  | Uvicorn / Localhost    |
| Architecture| Modular, API-driven    |

---

## 🛠️ Features Implemented

- `/score` endpoint for real-time credit scoring
- Pattern-based mock KYC validation
- `/pay` endpoint to simulate stablecoin loan disbursement
- Full loan form and UX in Streamlit
- Clear feedback and instant decisioning

---

## 🔁 Mapping Innovation to Code

- ✅ Manual underwriting → `/score` API (auto scoring)
- ✅ KYC/AML → mock national ID pattern validation
- ✅ Borderless lending → simulated `/pay` with USDC
- ✅ Instant approvals → frontend logic + backend response
- 🔜 On-chain records and data insights (planned)

---

## 🧠 Feedback Incorporated

- KYC/AML: mock check + Trulioo planned
- Default collection: smart contract logic + insurance model
- Real-time credit scoring via Open Banking logic
- Modular backend for region-specific licensing
- Synthetic data now, real API data later
- Blockchain for transparency + stablecoin logic

---

## 🔒 Risk Management

### Prerequisites for Scale
- Regulatory sandbox approval
- Cloud-native infrastructure
- Open Banking API partners
- Smart contract auditing pipeline

### Tech Risks
- Smart contract bugs
- API failure / stablecoin risk
- Data integrity

### Ops Risks
- Liquidity mismatch
- Data freshness
- Manual KYC fallback in some markets

### Security
- CAPTCHA & rate limiting
- Role-based access control
- Encryption + PII audit logs

---

## 📦 Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

**### 2. Start Backend**
```bash
uvicorn backend.main:app --reload
```

**### 3. Start Frontend on different terminal**
```bash
streamlit run frontend/app.py
```
