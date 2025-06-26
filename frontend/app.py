import streamlit as st
import requests

st.set_page_config(page_title="SMEily Lending Portal", page_icon="💸", layout="centered")
st.title("💸 SMEily Lending Platform")
st.caption("Empowering SMEs with fast, borderless, and transparent funding.")

st.header("📋 SME Loan Application")
with st.form("loan_form", border=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        business_type = st.selectbox("Business Type", ["Retail", "Tech", "Service", "Manufacturing", "Other"])
        country = st.text_input("Country")
    with col2:
        monthly_income = st.number_input("Monthly Revenue ($)", min_value=0.0, step=100.0)
        requested_amount = st.number_input("Loan Request ($)", min_value=0.0, step=100.0)
        national_id = st.text_input("National ID (starts with 'ID')")

    submitted = st.form_submit_button("Submit Application 💼")

##this is for the KYC checks 
if submitted:
    with st.spinner("Analyzing application and checking KYC..."):
        payload = {
            "name": name,
            "business_type": business_type,
            "monthly_income": monthly_income,
            "requested_amount": requested_amount,
            "country": country,
            "national_id": national_id
        }
        response = requests.post("http://localhost:8000/score", json=payload)
        result = response.json()

        st.divider()
        st.subheader("📊 Application Result")
        if "error" in result:
            st.error(f"❌ {result['error']}")
        else:
            st.success("✅ KYC Passed")
            st.metric(label="Credit Score", value=result['credit_score'])
## this is for the laon approavlas 
            if result["approved"]:
                st.success("🎉 Loan Approved!")
                if st.button("Simulate Stablecoin Payment (USDC)"):
                    pay_response = requests.post("http://localhost:8000/pay")
                    pay_data = pay_response.json()
                    with st.expander("💰 Payment Details"):
                        st.json(pay_data)
            else:
                st.warning("Loan Rejected. Try adjusting the amount or improving financials.")
