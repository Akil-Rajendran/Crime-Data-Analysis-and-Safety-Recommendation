import streamlit as st
import pandas as pd
import plotly.express as px

siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()
modelTraining = st.container()

with siteHeader:
    st.title('Safety Recommendation and Crime Prediction Tool')
    st.image('https://www.eurekaafricablog.com/wp-content/uploads/2018/09/Safety.jpg')
    # st.write('The crime dataset considered has crime data of all states in India for years 2001-2014')

with dataExploration:
    st.header('A 2-minute-read on crimes in India')
    by_place = pd.read_csv(r'by_place.csv', index_col=[0])
    dist_wise = pd.read_csv(r'dist_wise.csv', index_col=[0])
    state_group = pd.read_csv(r'state_group.csv', index_col=[0])
    st._transparent_write(""" 
        Location has a significant impact on crimes in India. Surprisingly, Bihar is the 10th most safe 
        state in India and holds better position than most of the more developed states. As of 2019, 
        Delhi had the highest crime rate (incidence of crime per 100,000 population) among all States of 
        India at 1586.1, rising steeply from 1342.5. Barring Kerala(1287.7), all other states and union 
        territories had a significantly lower crime rate. Contrary to popular belief, the most populous 
        state of Uttar Pradesh only had the 16th highest crime rate in the country. This is a steep drop 
        from 2015 when the state had an overall crime rate of 1293. States in Northeast India have 
        consistently reported much lower crime rates, with 4 of the 5 states having the lowest crime in 
        being from the region. Uttar Pradesh reported the highest incidence of violent crimes accounting 
        for 15.2% of total violent crimes in India (65,155 out of 4,28,134) followed by Maharashtra (10.7%),
        and Bihar and West Bengal each accounting for 10.4% of such cases.
    """)
    st.header('Sample from the state_group dataset')
    st.write(state_group.sample(20))
    st.header('Sample from the by_place dataset')
    st.write(by_place.sample(10))
    st.header('Sample from the dist_wise dataset')
    st.write(dist_wise.sample(10))

# with newFeatures:


# with modelTraining: