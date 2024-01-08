import streamlit as st
import plotly.express as px 
import pandas as pd
st.set_page_config(page_icon='🛫' , page_title = 'Airline Dashboard')

df = pd.read_csv('Airline_edite.csv')


tab , tab2 , tab3= st.tabs(['Data descriptive','catigorical charts','nomerical charts'])
###########################################################_TAB_######################################################################################
with tab :
    st.markdown('<h3 style="text-align: center; color :#1450DB;">descriptive stat and Dataset</h3>',unsafe_allow_html=True)
    st.dataframe(df)
    col1 , col2 , col3 = st.columns([1,0.15,1])
    with col1 :
        st.markdown('<h4 style="text-align: center; color :green;">descriptive stat(numirec)</h3>', unsafe_allow_html=True)
        numeric_data = df.select_dtypes(include=['number'])
        st.dataframe(numeric_data.describe())
    with col3 :
        st.markdown('<h4 style="text-align: center; color :red;">descriptive stat(catigorec)</h3>', unsafe_allow_html=True)
        categorical_data = df.select_dtypes(include=['object'])
        st.dataframe(categorical_data.describe())

################################################################_TAB2_###################################################################################
with tab2 :
    columns = [None]+categorical_data.columns.to_list()
    col1 , col2 , col3 = st.columns([1,0.10,1])
    with col1 :
        x = st.selectbox('select x column:',columns)
    with col3 :
        color = st.selectbox('''do want coloring?!
        select color baised on eny column from here:''',columns)
    if x !=None:
        if color != None:
            st.plotly_chart(px.histogram(categorical_data,x=x,color=color,text_auto = True,title = f'Histogram for {x}'),use_container_width=True)
        elif color ==None :
            st.plotly_chart(px.histogram(df,x=x,color=x,text_auto=True,title=f'Histogram for {x}') , use_container_width=True)
        co , co1 , co2 = st.columns([1,0.10,1])
        with co :
            st.plotly_chart(px.sunburst(df,path = [x] , title = f'sunburst chart for {x} column'), use_container_width=True)
        with co2 :
            st.plotly_chart(px.pie(df,names = x , title = f'pie chart for {x} column'))

        st.plotly_chart(px.treemap(df,path=[x],color = x , title=f'Treemap for {x}'),use_container_width=True)
    else :
        None

#################################################################_TAB3_##################################################################################
    
with tab3 :
    x2 = st.selectbox('select colomun from here',[None]+numeric_data.columns.to_list())
    if x2 != None :
        st.plotly_chart(px.histogram(df,x=x2 , title=f'Histogram for {x2}'),use_container_width=True)
    else :
        None
    col , col1 , col2 = st.columns([1,0.10,1])
    with col:
        y = st.selectbox('select y column thats contain numerical data to be clear for your eyes',[None]+numeric_data.columns.to_list())
    with col2 :
        x3 = st.selectbox('select x  column for scatter plot' ,[None]+categorical_data.columns.to_list())
    if y != None :
        st.plotly_chart(px.scatter(df,x=x3,y=y , color=color,title=f'Scattar for {y}'),use_container_width=True)
    else :
        None