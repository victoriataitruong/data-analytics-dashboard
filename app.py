import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np  # Import numpy separately

# Simulated Sample Data (replace with your own dataset or provide sample data)
def load_sample_data():
    # Sample data for demonstration, replace this with the path to your actual file if needed
    data = {
        'Date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
        'Sales': np.random.randint(50, 500, size=100),  # Use numpy for random values
        'Profit': np.random.randint(10, 100, size=100)  # Use numpy for random values
    }
    df = pd.DataFrame(data)
    return df

# Streamlit page configuration
st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

# Title of the app
st.title("Victoria's Interactive Data Analytics Dashboard")

# Description of the app
st.markdown("""
This app simulates file loading and provides interactive data analysis using sample data.
Click the button below to load the sample dataset and view visualizations.
""")

# Load sample data when the button is clicked
if st.button('Generate Random Sample Data'):
    df = load_sample_data()
    st.success("Sample data loaded successfully!")

    # Display basic statistics
    st.subheader("Data Summary")
    st.write(df.describe())

    # Display DataFrame
    st.subheader("Data Preview")
    st.write(df.head())

    # Interactive chart for Sales and Profit over time
    st.subheader("Sales and Profit Trend")
    fig = px.line(df, x='Date', y=['Sales', 'Profit'], title='Sales and Profit Over Time')
    st.plotly_chart(fig)

    # Histogram of Sales
    st.subheader("Sales Distribution")
    fig = px.histogram(df, x='Sales', nbins=20, title="Distribution of Sales")
    st.plotly_chart(fig)

    # Scatter plot for Profit vs Sales
    st.subheader("Profit vs Sales")
    fig = px.scatter(df, x='Sales', y='Profit', title="Profit vs Sales")
    st.plotly_chart(fig)

else:
    st.info("Click the button to load the sample data.")
