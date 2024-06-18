import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import datetime



st.title("Stock Data Viz")

ticker_symb = st.text_input("Ticker Name", value = "AAPL")
ticker_data = yf.Ticker(ticker_symb)


dc1, dc2 = st.columns(2)

with dc1:
    start = st.date_input("Start Date", datetime.date(2019,7,6))
with dc2:
    end = st.date_input("Start Date", datetime.date(2019,8,10))

ticker_df = ticker_data.history(period = '1mo', start = start, end = end)

col1, col2 = st.columns(2)
# st.dataframe(ticker_df, use_container_width=True)
with col1:
    st.subheader("Daily Close Line Chart")
    st.line_chart(data=ticker_df.reset_index(), x="Date", y="Close",)

with col2:
    st.subheader("Daily Volume Line Chart")
    st.line_chart(data=ticker_df.reset_index(), x="Date", y="Volume")
