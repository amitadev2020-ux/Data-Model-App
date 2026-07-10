import streamlit as st
import pandas as pd
import io

st.title("Dataset Viewer")

df = pd.read_csv("dataset9000.csv")

st.write("## Dataset")
st.dataframe(df)

st.write("## Last 5 Rows")
st.dataframe(df.tail())

st.write("## Shape")
st.write(df.shape)

st.write("## Columns")
st.write(df.columns.tolist())

st.write("## Dataset Info")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

st.write("## Missing Values")
st.write(df.isnull().sum())

st.write("## Statistics")
st.write(df.describe())

df.to_csv("new_dataset.csv", index=False)
