import streamlit as st
import pandas as pd
st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# Racer Page 🎈")

st.write(' # Mariokart *Stats Website*')

df_racer = pd.read_csv ('/workspaces/streamlit_app/data/racer_stats.csv')

st.write(df_racer)

st.dataframe(df_racer.style
            .highlight_max(color='lightgreen', axis=0,subset=['Speed', 'Acceleration', 'Weight', 'Handling', 'Traction/Grip', 'Mini-Turbo', 'Times First Place', 'Total Races'])
            .highlight_min(color='red', axis=0,subset=['Speed', 'Acceleration', 'Weight', 'Handling', 'Traction/Grip', 'Mini-Turbo', 'Times First Place', 'Total Races']))
st.line_chart(df_racer,x='Speed',y=['Acceleration','Weight','Times First Place'])
st.header("Racer speed does not seem to correlate to number of races won")
x = st.slider( 'How Many Racers to Show',1,len(df_racer))

st.write("Racers by Speed")
df_fastest_racers = df_racer[['Character','Speed']].sort_values("Speed",ascending=False).iloc[0:x]
st.dataframe(df_fastest_racers)