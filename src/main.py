import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
from copy import deepcopy

###################################################################################
### LOADING FILES

# Load data downloaded from FAO



# LOAD DATAFRAME FUNCTION
def load_data(path):
    df = pd.read_csv(path)
    return df


# LOAD GEOJSON FILE
with open("./data/countries.geojson") as response:
    countries = json.load(response)

# LOAD TEMPERATURE DATA
df_raw = load_data(path="data/temp_gdppc.csv")
df = deepcopy(df_raw)

# LOAD EMISSIONS DATA
df_e_raw = load_data(path="data/TOT_EMpc_DF.csv")
df_e = deepcopy(df_e_raw)

# Format the page with less spaces on the side
st.set_page_config(layout="wide")

# Add title and header
st.title("Climate change")
st.header("Detail per Country")

## Geographic Maps
#Temperature change standard deviation from 1961
fig1 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df.Area,
                                    z= df['Std_temp'],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255,255,255)'], [0.5, 'rgb(255,136,0)'], [1, 'rgb(255,0,0)']],
                                    zmax = df['Std_temp'].max(),
                                    text=df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
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
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig2.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#CO2 per capita
fig3 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df_e.Area,
                                    z=df_e["CO2pc"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df["CO2pc"].max(),
                                    text = df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig3.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#N2o per capita
fig4 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df.Area,
                                    z=df["N20pc"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df["CO2pc"].max(),
                                    text = df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig4.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#CH4 per capita
fig5 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df.Area,
                                    z=df["CH4pc"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df["CH4pc"].max(),
                                    text = df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig5.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#Normalized total emissions
fig6 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df.Area,
                                    z=df["Total_n_emissions"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df["Total_n_emissions"].max(),
                                    text = df.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig6.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig6.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# Creating the dropdown selector
option = st.selectbox(
	'Choose the map to see',
	('Temperature change standard deviation from 1961',
	'GDP per capita in 2020',
	'Co2 emissions in 2018 (TONS PER PERSON)',
	'N2o (Nitrous oxide) emissions in 2018 (TONS PER PERSON)',
	'CH4 (Methane) emission in 2018 (TONS PER PERSON)',
	'Total Emissions in 2018 (normalized indicator)'
	))

if option == 'Temperature changes':
	st.plotly_chart(fig1)

if option == 'GDP per capita in 2020':
	st.plotly_chart(fig2)

if option == 'Co2 emissions in 2018 (TONS PER PERSON)':
	st.plotly_chart(fig3)

if option == 'N2o (Nitrous oxide) emissions in 2018 (TONS PER PERSON)':
	st.plotly_chart(fig4)
	
if option == 'CH4 (Methane) emission in 2018 (TONS PER PERSON)':
	st.plotly_chart(fig5)

if option == 'Total Emissions in 2018 (normalized indicator)':
	st.plotly_chart(fig6)

# Setting up columns
c1,c3 = st.columns([1,1])


link = '[To see the code in GitHub ](https://github.com/AdriPerse/climate-change)'
c3.markdown(link, unsafe_allow_html=True)
