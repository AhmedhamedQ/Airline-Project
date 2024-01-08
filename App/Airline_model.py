import streamlit as st
import pandas as pd 
import numpy as np
import joblib

st.set_page_config(page_title='Airline Model' , page_icon='🛫')

model = joblib.load('KNN_model.pkl')
df = pd.read_csv('Airline.csv')

def Prediction(Airline,month,Source,Destination,Route,Duration,Total_Stops,Additional_Info):
       x = pd.DataFrame(columns=['Airline', 'month(2019)', 'Source', 'Destination', 'Route', 'Duration',
       'Total_Stops', 'Additional_Info'])

       x.at[0,'Airline'] = Airline
       x.at[0,'month(2019)'] = month
       x.at[0,'Source'] = Source
       x.at[0,'Destination'] = Destination
       x.at[0,'Route'] = Route
       x.at[0,'Duration'] = Duration
       x.at[0,'Total_Stops'] = Total_Stops
       x.at[0,'Additional_Info'] = Additional_Info
       return f'The ticket price is approximately = {np.round(model.predict(x)[:],2)} .'

co1 , co2 , co3 = st.columns([1,0.10,1])
with co1 :
     st.image("indian-pacific-logo.png" , use_column_width=True)
with co3 :
     st.header('Price prediction:')
     st.write('This model predict the price of tickets.Experimental copy(tarin on a small data)')
col , col2 , col3 = st.columns([1,0.010,1])
with col :
    Airline = st.selectbox('Select Airline',df['Airline'].unique().tolist())
    month = st.selectbox('Select month of the year' , df['month(2019)'].unique().tolist())
    Source = st.selectbox('Select Source' , df['Source'].unique().tolist())
    Destination = st.selectbox('Select Destination' , df['Destination'].unique().tolist())

with col3 :
    Route = st.selectbox('Select Route',df[(df['Source']==Source)&(df['Destination']==Destination)]['Route'].unique().tolist())
    Duration = st.slider('Duration of trip',min_value = 45 , max_value = df['Duration'].max()+30 , value = df[df['Route']==Route]['Duration'].to_list()[0], step = 1)
    Total_Stops = st.slider('Total Stops',min_value = df['Total_Stops'].min() , max_value = df['Total_Stops'].max() , value = df[df['Route']==Route]['Total_Stops'].to_list()[0] , step = 1)
    Additional_Info = st.selectbox('Additional Info', df['Additional_Info'].unique().tolist())

if st.button('Pridect'):
    st.write(Prediction(Airline,month,Source,Destination,Route,Duration,Total_Stops,Additional_Info))
    st.warning('Please note that this is an estimate and may be higher or lower than the actual price.')
else :
     st.write('Please fill data')
