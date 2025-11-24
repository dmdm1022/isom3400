import streamlit as st
import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv')

# Read the CSV file into a DataFrame
# Declare delimiter based on how the csv is formatted
df1 = pd.read_csv(file_path, delimiter=';')

# Display the DataFrame in an interactive table
st.write("Wine Quality Data")
st.dataframe(df1)

################################

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}
df2 = pd.DataFrame(data)

# Show data with Streamlit elements
st.dataframe(df2)                # Interactive table
st.data_editor(df2)              # Editable table
st.table(df2)                    # Static table

# Customize columns directly in the dataframe display
st.dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers': '{:,.0f}'}))
