#The following block of code handles library importation

import streamlit as st
import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

df = pd.read_csv('Global_Visualization/First_edit.csv')


st.title('GLOBAL METRICS')

st.caption(":blue[A simple web app that visualizes selected metrics for countries of the world]")

st.text("HOW TO USE. \n1.Select the metric you want to visualize \n2.Click the submit button")





#HANDLING THE USER INPUT
form = st.form("User_Choice")
choice = form.selectbox("Select the metric to be visualized: ",['','Population','Unemployment','GDP per Capita','Surface Area'])
form.form_submit_button("Submit")


#CREATING THE POPULATION PLOT
if choice == 'Population':
    population_data = dict(type = 'choropleth',
               colorscale = 'ylorrd',
               locations = df['Country'],
               locationmode = 'country names',
               z = df['Population in thousands (2017)'],
               colorbar = {'title': 'Population in thousands (2017)'})
    
    
    population_layout = go.Layout(dict(title = 'Population(in thousands) of countries of the world 2017',geo = dict(scope = 'world')))
    
    population_fig = go.Figure(population_data,population_layout)
    
    plot(population_fig)
    



#CREATING THE UNEMPLOYMENT PLOT
elif choice == "Unemployment":
    unemployment_data = dict(type = 'choropleth',
           colorscale = 'ylorrd',
           locations = df['Country'],
           locationmode = 'country names',
           z = df['Unemployment (% of labour force)'],
           colorbar = {'title': 'Unemployment (% of labour force)'})
    
    unemployment_layout = go.Layout(dict(title = 'Unemployment (% of labour force)',geo = dict(scope = 'world')))
    
    unemployment_fig = go.Figure(unemployment_data,unemployment_layout)
    plot(unemployment_fig)
    
    

 
    
 
#CREATING THE GDP PLOT
elif choice == "GDP per Capita":
    gdp_data = dict(type = 'choropleth',
           colorscale = 'ylorrd',zmin = 0, zmax = 70000,
           locations = df['Country'],
           locationmode = 'country names',
           z = df['GDP per capita (current US$)'],
           colorbar = {'title': 'GDP per capita (current US$)'})
    
    gdp_layout = go.Layout(dict(title = 'GDP per capita (current US$) of countries of the world 2017',geo = dict(scope = 'world')))
    gdp_fig = go.Figure(gdp_data,gdp_layout)
    plot(gdp_fig)
    



#CREATING THE SURFACE AREA PLOT
elif choice == "Surface Area":
    area_data = dict(type = 'choropleth',
           colorscale = 'ylorrd',
           locations = df['Country'],
           locationmode = 'country names',
           z = df['Surface area (km2)'],
           colorbar = {'title': 'Surface area (km2)'})
    
    area_layout = go.Layout(dict(title = 'Surface area(in km2) of countries of the world 2017',geo = dict(scope = 'world')))
    area_fig = go.Figure(area_data,area_layout)
    plot(area_fig)
