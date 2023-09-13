import streamlit as st
import pandas as pd
import altair as alt


st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")


st.write("What Kart Configuration is Best?")


df_kart = pd.read_csv('/workspaces/streamlit_app/data/kart_stats.csv')


columns_to_display = ['Body', 'Weight', 'Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed', 'Ground Handling']


st.dataframe(
    df_kart[columns_to_display]
    .style
    .highlight_max(color='lightgreen', axis=0, subset=columns_to_display)
    .highlight_min(color='red', axis=0, subset=columns_to_display)
)

c = alt.Chart(df_kart).mark_circle().encode(
    x='Ground Speed',
    y='Weight',
    size='Acceleration',
)

st.altair_chart(c, use_container_width=True)

st.line_chart(df_kart,x='Acceleration',y=['Mini-Turbo','Ground Handling'])

chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])

df_single_kart = df_kart[df_kart['Body'] == chosen_kart].drop(columns=['Body'])

df_unp_kart = df_single_kart.unstack().rename_axis(['category', 'row number']).reset_index().drop(columns='row number').rename({0: 'strength'}, axis=1)

st.bar_chart(df_unp_kart, x='category', y='strength')
