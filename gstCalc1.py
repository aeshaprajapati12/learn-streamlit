import streamlit as st
st.set_page_config(
    page_title="GST Calculator",
    page_icon="🧾",
    layout="wide"
)

st.title("🧾 GST Calculator")
st.write("Calculate GST by selecting the amount, GST rate, and tax type.")

st.divider()

col1,col2,col3 = st.columns(3)

with col1:
    amount = st.number_input(
        "Amount",
        min_value=0.0,
        value=10000.0,
        step=100.0
    )

with col2:
    gst = st.selectbox(
        "GST_%",
        [0,5,12,18,25,40],
        index = 2
    )

with col3:
    choice = st.selectbox(
        "Tax_type",
        ["Inclusive",
        "Exclusive"]
    )

st.divider()


if choice == "Exclusive":

    gst_amount = amount * gst / 100
    actual_amount = amount
    total_amount = amount + gst_amount

else:

    actual_amount = amount * (100 / (100 + gst))
    gst_amount = amount - actual_amount
    total_amount = amount

c1,c2,c3,c4,c5 = st.columns([4,1,4,1,4])

with c1:
    st.metric(
        "actual_amount",
        f"₹ {actual_amount}"
    )

with c2:
    st.markdown("## +")

with c3:
    st.metric("GST",
          f"{gst}%"
        )
    
with c4:
    st.markdown("## =")
    
with c5:
    st.metric(
        "total_amount",
        f"₹ {total_amount}"
    )

st.divider()


st.subheader("Summary")

st.table({
    "Description": [
        "Amount Entered",
        "GST Rate",
        "Tax Type",
        "GST Amount",
        "Actual Amount",
        "Total Amount"
    ],
    "Value": [
        f"₹ {amount:,.2f}",
        f"{gst}%",
        choice,
        f"₹ {gst_amount:,.2f}",
        f"₹ {actual_amount:,.2f}",
        f"₹ {total_amount:,.2f}"
    ]
})

