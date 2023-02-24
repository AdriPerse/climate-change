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
#@st.cache
#@st.experimental_memo


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

# LOAD SDG DATA
all_sorted_raw = load_data(path="/data/all_sorted.csv")
all_sorted = deepcopy(all_sorted_raw)

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
                                    zmax = df_e["CO2pc"].max(),
                                    text = df_e.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig3.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#N2o per capita
fig4 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df_e.Area,
                                    z=df_e["N20pc"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df_e["CO2pc"].max(),
                                    text = df_e.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig4.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#CH4 per capita
fig5 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df_e.Area,
                                    z=df_e["CH4pc"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df_e["CH4pc"].max(),
                                    text = df_e.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig5.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#Normalized total emissions
fig6 = go.Figure(go.Choroplethmapbox(geojson=countries,
                                    locations=df_e.Area,
                                    z=df_e["Total_n_emissions"],
                                    featureidkey="properties.ADMIN",
                                    colorscale=[[0, 'rgb(255, 255, 255)'],
                                                [0.5, 'rgb(255, 0, 0)'],
                                                [1, 'rgb(0,0,0)']],
                                    zmax = df_e["Total_n_emissions"].max(),
                                    text = df_e.Area,
                                    hovertemplate="Country: %{text}<br> %{z}"'<extra></extra>',
                                    marker_opacity=0.7,
                                    marker_line_width=0))

fig6.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1)
fig6.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# Creating the dropdown selector
option = st.selectbox(
	'Choose the map to see',
	('Temperature change standard deviation from 1961 per year',
	'GDP per capita in 2018',
	'Co2 emissions in 2018 (TONS PER PERSON)',
	'N2o (Nitrous oxide) emissions in 2018 (TONS PER PERSON)',
	'CH4 (Methane) emission in 2018 (TONS PER PERSON)',
	'Total Emissions in 2018 (normalized indicator)'
	))

if option == 'Temperature change standard deviation from 1961 per year':
	st.plotly_chart(fig1)

if option == 'GDP per capita in 2018':
	st.plotly_chart(fig2)

if option == 'Co2 emissions in 2018 (TONS PER PERSON)':
	st.plotly_chart(fig3)

if option == 'N2o (Nitrous oxide) emissions in 2018 (TONS PER PERSON)':
	st.plotly_chart(fig4)
	
if option == 'CH4 (Methane) emission in 2018 (TONS PER PERSON)':
	st.plotly_chart(fig5)

if option == 'Total Emissions in 2018 (normalized indicator)':
	st.plotly_chart(fig6)

###############################################################################
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')

#Prepare data plot
all_sorted.drop([0], axis = 0, inplace=True, errors = 'ignore')
all_sorted.drop([1], axis = 0, inplace=True, errors = 'ignore')
all_sorted['index'] = all_sorted['oce20'] + all_sorted['ter20'] + all_sorted['wat20']
all_sorted['index_n'] = (all_sorted['index'] * 100)/255.51

#Widget
st.markdown('<div style="text-align:center; font-size:20px; font-weight:bold;">CO\u2082 emissions from fossil fuel and cement production and SDG index compliance</div>', unsafe_allow_html=True)
sdgs = ['CO2'] + ['Index']
sdg = st.selectbox('Choose country option', sdgs)

#Control flow plot
if sdg == 'CO2':
    plot = px.bar(all_sorted[:70], x='co20', y='Country', color = 'co20', height=700, range_x=(1.5, 18), width=None, color_continuous_scale = 'RdYlGn_r', orientation='h')
    st.plotly_chart(plot, use_container_width=True)

elif sdg == 'Index':
    all_sorted_index = all_sorted.sort_values("index_n", ascending=False).reset_index(drop=True)
    plot = px.bar(all_sorted_index[:100], x='index_n', y='Country', color = 'co20',range_x=(40, 100), height=700, width=None, orientation='h', color_continuous_scale = 'RdYlGn_r')
    st.plotly_chart(plot, use_container_width=True)

st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')
#####################################################################
# Setting up columns for links
c1,c3 = st.columns([1,1])


link = '[To see the code in GitHub ](https://github.com/AdriPerse/climate-change)'
c3.markdown(link, unsafe_allow_html=True)
