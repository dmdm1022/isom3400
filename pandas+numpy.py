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
st.write("st.dataframe(df2)")
st.dataframe(df2)                # Interactive table

st.write("st.data_editor(df2)")
st.data_editor(df2)              # Editable table

st.write("st.table(df2)")
st.table(df2)                    # Static table

# Customize columns directly in the dataframe display
st.write("customized formatting")
st.dataframe(df2.style.format({'Sales': '${:,.0f}', 'Customers': '{:,.0f}'}))

################################

# Step 1: Install Streamlit (run in terminal: pip install streamlit)

# Step 2: Import Necessary Libraries
import streamlit as st
import numpy as np
import pandas as pd

# Step 3: Generate Random Sales Data
sales_data = np.random.rand(100) * 1000

# Step 4: Create a DataFrame
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.random.rand(5) * 1000
customers = np.random.randint(1, 100, size=5)

df3 = pd.DataFrame({
    'Product': products,
    'Sales': sales,
    'Customers': customers
})

# Step 5: Visualize Sales Data

# Display DataFrame using st.dataframe
st.markdown("### Product Sales and Customer Data")
st.dataframe(df3)  # Interactive table with sorting and resizing

# Line Chart - Sales Over Time
st.markdown("### Sales Over Time")
st.line_chart(sales_data)

# Area Chart - Cumulative Sales
st.markdown("### Cumulative Sales")
st.area_chart(sales_data)

# Bar Chart - Sales by Product
st.markdown("### Sales by Product")
st.bar_chart(df3[['Product', 'Sales']].set_index('Product'))

# Scatter Chart - Customer Engagement by Product
st.markdown("### Customer Engagement by Product")
st.scatter_chart(df3[['Product', 'Customers']].set_index('Product'))

# Step 6: Run the Streamlit App (run in terminal: streamlit run app.py)
