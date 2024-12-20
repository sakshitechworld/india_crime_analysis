

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import load_crime_data
import ipywidgets as widgets
from ctypes import alignment
from dynamic_kpis.crime_trends_over_years import crime_trends_over_years
from dynamic_kpis.each_crime_category_over_years import each_crime_category_over_years

def dynamic_insights():
        
    df = load_crime_data()
    crime_trends_over_years(df)
    each_crime_category_over_years(df)


   


    # #3.States with Top 5 Crime Types
    # crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
    #                 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
    #                 'Other Crimes Against SCs']

    # unique_states = df['STATE/UT'].unique()

    # # Create a dropdown widget for state selection
    # state_dropdown = widgets.Dropdown(
    #     options=unique_states,
    #     value=unique_states[0],  # Default to the first state
    #     description='Select State:'
    # )

    # # Function to update the pie chart based on state selection
    # def update_pie_chart(state):
    #     # Filter the DataFrame based on the selected state
    #     state_df = df[df['STATE/UT'] == state]

    #     # Calculate the sum of each crime type for the selected state
    #     crime_type_sums = state_df[crime_type_cols].sum()
    #     crime_type_sums = crime_type_sums[crime_type_sums > 0]
    #     if not crime_type_sums.empty:
    #     # Select the top 5 crime types with the highest occurrences
    #         top_5_crimes = crime_type_sums.nlargest(5)
    #         fig = plt.figure(figsize=(8, 8))
    #         plt.pie(top_5_crimes, labels=top_5_crimes.index, autopct='%1.1f%%', startangle=140)
    #         plt.title(f"Top 5 Crime Types in {state}")
    #         st.pyplot()
    #     else:
    #         print(f"No data found for {state} for crime types")
    # # Link the dropdown widget to the chart update function
    # widgets.interactive(update_pie_chart, state=state_dropdown)
