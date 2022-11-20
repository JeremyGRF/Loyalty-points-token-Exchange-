import streamlit as st

st.set_page_config(
    page_title="Loyalty Exchange Program",
    page_icon="👋",
)

st.write("# Welcome to Loyalty Exchange! 👋")

st.sidebar.success("Select a service above.")

st.markdown(
    """
    Loyalty Exchange Program is a decentralized and standardized system 
    that will allow users to swap reward points or the tokens from different 
    stores and to spend as if they are one loyalty program
    **👈 Select a brand/service from the sidebar** 
    ### Demo Brands
    - Best Buy
    - Delta
    - Nike
    - Starbucks
    ### Demo Services
    - Transfer
    - Deposit
"""
)

