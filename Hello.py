import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

ra=pd.read_csv('fifa.csv')
rs=pd.read_csv('results.csv')

st.title('History of matches')

Home = st.selectbox(
    'Home Team:',
    ('England', 'France', 'Italy'))


Away = st.selectbox(
    'Away Team:',
    ('France', 'England', 'Italy'))


newra=rs[(rs['home_team'] == Home) & (rs['away_team'] == Away)]

st.dataframe(newra)


dfEn=ra[ra['country_full'] == 'England']
dfFR=ra[ra['country_full'] == 'France']
dfIt=ra[ra['country_full'] == 'Italy']

st.title('Fifa Ranking')

show_curve1 = st.checkbox('England', value=True)
show_curve2 = st.checkbox('France', value=True)
show_curve3 = st.checkbox('Italy', value=True)

fig, ax = plt.subplots()
if show_curve1:
    plt.plot(dfEn['rank_date'], dfEn['rank'],label='England')
if show_curve2:
    plt.plot(dfFR['rank_date'], dfFR['rank'],label='France')
if show_curve3:
    plt.plot(dfIt['rank_date'], dfIt['rank'],label='Italy')

plt.xlabel('Date')
plt.ylabel('Ranking')
new_ticks = [1, 50, 100, 150,200, 250 ,290, 326]  # Specify the tick positions
new_labels = ['1992', '1998', '2002', '2007', '2011','2015', '2019', '2023']  # Specify the corresponding labels
plt.xticks(new_ticks, new_labels)
plt.title('Ranking over time')
plt.legend()
st.pyplot(fig)



