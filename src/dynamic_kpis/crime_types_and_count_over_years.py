
import streamlit as st
import ipywidgets as widgets
from utils import crime_columns
import matplotlib.pyplot as plt


def crime_types_and_count_over_years(df):
 
    st.subheader("Crime Types & Count Over Years")
    st.text("Author: Aniket Agarkar")
 
    unique_states = df['STATE/UT'].unique()

    min_year = df['Year'].min()
    max_year = df['Year'].max()

    # Create dropdown widget for state selection
    selected_state = st.selectbox("Select State To Analyse Accross States", options=unique_states)  
    selected_year = st.slider("Select Year To Analyse Accross States", min_value=min_year, max_value=max_year, value=min_year, step=1)
    state_df = df[(df['STATE/UT'] == selected_state) & (df['Year'] == selected_year)]
    total_crimes_per_year = state_df[crime_columns].sum()

    if not total_crimes_per_year.empty:  # Check if data exists for the selection

        # Create a bar chart


        fig = plt.figure(figsize=(10, 6))

        plt.bar(total_crimes_per_year.index, total_crimes_per_year.values,color = 'Orange')

        plt.xlabel('Crime Type')
        plt.ylabel('Total Crimes')

        plt.title(f'Crime Types and Counts in {selected_state} for Year {selected_year}')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        st.pyplot(fig)

    else:
        print(f"No data found for {selected_state} in year {selected_year}.")


