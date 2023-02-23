import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
from copy import deepcopy

###################################################################################
### LOADING FILES

# Load data downloaded from data.open-power-system-data.org/renewable_power_plants/2020-08-25
@st.experimental_memo

# LOAD DATAFRAME
df = pd.read_csv("../../data/gdppc20_clean.csv")

# LOAD GEOJSON FILE
with open("../../data/countries.geojson") as response:
    countries = json.load(response)


# Add title and header
st.title("Climate change")
st.header("Detail per Country")

## Geographic Maps
#Temperature standard deviation
fig1 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df.Area,
                                    z= df.Std_temp,
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255,255,255)'], [0.5, 'rgb(255,136,0)'], [1, 'rgb(255,0,0)']],
                                    zmax = df['Std_temp'].max(),
                                    text=df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    #labels={m_std_df.Value: 'Standard deviation<br> Temperature change'},
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig1.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#GDP per capita
fig2 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df.Area,
                                    z=df["GDPpc"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.1, 'rgb(13, 255, 174)'],
                                                
                                                [0.3, 'rgb(77, 252, 255)'],
                                                
                                                [0.7, 'rgb(77, 104, 255)'],
                                                [1, 'rgb(255,0,0)']],
                                    zmax = df["GDPpc"].max(),
                                    text=df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    #labels={m_std_df.Value: 'Standard deviation<br> Temperature change'},
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig2.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

option = st.selectbox(
...     'How would you like to be contacted?',
...     ('Temperature changes', 'GDPpc', 'Co2'))

if option == 'Temperature changes':
    st.plotly_chart(fig1)
    if option == 'GDPpc':
        st.plotly_chart(fig2)

 Setting up columns
c1,c3 = st.columns([1,1])


link = '[To see the code in GitHub ](https://github.com/AdriPerse/climate-change)'
c3.markdown(link, unsafe_allow_html=True)