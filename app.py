import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV data
df = pd.read_csv("Test data.csv")

# Title of the report
st.title("Performance Evaluation of Air Cooler")

# Introduction
st.write("""The objective of this evaluation was to estimate the quality of our 
         products in terms of performance and reliability. Several series of experiments
          were conducted within a specified time frame, evaluating the performance of an 
         air cooler under various temperature and humidity conditions. The experiments took 
         place in an isolated room to maintain a controlled environment.
""")

# Experiment Details
st.subheader("Experiment Details:")
st.write("The experiments were conducted over half an hour, with data collected for every minute change.")
st.write("The recorded parameters include:")

    # Parameters List

st.write("- Time: The time elapsed in Minutes.")
st.write("- Dry Bulb Temp: The room temperature measured with a digital thermometer that does not account for relative humidity.")
st.write("- Wet Bulb Temp: The temperature measured with a digital thermometer that takes into account the relative humidity.")
st.write("- Humidity: The relative humidity of the room.")        
st.write("- Outlet Temp : The temperature of the outlet air from the cooler.")
st.write("- Inlet Temp : The temperature of the inlet air to the cooler.")
st.write("- Change in Inlet and Outlet Temp: The difference between the inlet and outlet temperature of the cooler. The difference between the outlet temperature of the cooler and the room temperature.")


# 1. Change in Inlet and Outlet Trend Over Time
st.subheader("1. Change in Inlet and Outlet Temperature Trend Over Time")

fig2 = px.line(df, x='Time', y='Change',
              labels={'Change': 'Change'},
              range_y=[3, 12],
              range_x=[0, 31],
              hover_data=['Time', 'Change'],
              width=600, height=300)

st.plotly_chart(fig2)

st.subheader("Observations on Change in Inlet and Outlet:")
st.write("""TThe primary purpose of our air cooler is to provide cool air and reduce room temperature. 
         To measure the product's cooling capacity, we conducted experiments to observe the Change in 
         Inlet and Outlet Temperature Trend. The results indicated a consistent increase in the 
         temperature difference between the inlet and outlet, ranging from 4.5°C to 11°C. This suggests that the cooler effectively 
         maintained its output despite fluctuations in ambient temperature and humidity.""")
st.subheader("")

# 2. Humidity Trend Over Time
st.subheader("2. Humidity Trend Over Time")
fig = px.line(df, x='Time', y='Humidity',
              labels={'Humidity': 'Humidity'},
              range_y=[45, max(df['Humidity']) + 5],
              range_x=[0, 31],
              hover_data=['Time', 'Humidity'],
              width=600, height=300)

st.plotly_chart(fig)

st.subheader("Observations on Humidity Trend:")
st.write("""Humidity plays a crucial role in creating a suitable living environment 
         when using air coolers to decrease room temperature. Our goal was to ensure 
         our product can maintain optimal humidity levels. Observations on Humidity 
         Trend revealed that the cooler effectively increased humidity from 49.3 g/kg to 62.67 g/kg, 
         providing a comfortable living environment. Additionally,
        the product addressed the issue of stickiness associated with increased humidity.""")
st.subheader("")

# 3. Dry Bulb Temp of Room VS Wet Bulb Temp Trend Over Time
st.subheader("3. Dry Bulb Temp VS Wet Bulb Temp Trend Over Time")


chart3 = alt.Chart(df).mark_line().encode(
    x='Time:Q',
    y=alt.Y('dry bulb:Q', scale=alt.Scale(domain=[18, max(df['dry bulb']) + 0.1])),
    color=alt.value('blue'),
    tooltip=['Time:T', 'dry bulb:Q']
) + alt.Chart(df).mark_line().encode(
    x='Time:Q',
    y='wet bulb:Q',
    color=alt.value('green'),
    tooltip=['Time:T', 'wet bulb:Q']
).properties(width=600, height=300)
# Display a custom legend
st.subheader("")

st.markdown("- Dry Bulb Temperature: Blue")
st.markdown("- Wet Bulb Temperature: Green")

# Add a legend
chart3 = chart3.encode(color=alt.Color('legend:N', scale=alt.Scale(scheme='category10')))

st.altair_chart(chart3, use_container_width=True)
st.subheader("Observations on Dry bulb VS Wet bulb:")
st.write("""Evaluating temperature with respect to humidity was achieved by comparing 
         Wet Bulb and Dry Bulb temperatures. The aim was to calculate temperature changes
          considering humidity and assess performance in relation to both humidity and 
         temperature. Observations on Dry Bulb Temp VS Wet Bulb Temp revealed a gradual 
         decline in dry bulb temperature to approximately 26°C and a corresponding 
         decrease in wet bulb temperature from 23°C to 20°C over the 30-minute period.""")
st.subheader("")

# 4. Wet Bulb Temp of Room VS Output Trend Over Time
st.subheader("4. Wet Bulb Temp VS Outlet Temp Trend Over Time")
st.markdown("- Output Temperature: Blue")
st.markdown("- Wet Bulb Temperature: Green")
chart4 = alt.Chart(df).mark_line().encode(
    x='Time:Q',
    y=alt.Y('wet bulb:Q', scale=alt.Scale(domain=[18, max(df['wet bulb']) + 5])),
    color=alt.value('blue'),
    tooltip=['Time:T', 'wet bulb:Q']
) + alt.Chart(df).mark_line().encode(
    x='Time:Q',
    y='Output:Q',
    color=alt.value('green'),
    tooltip=['Time:T', 'Output:Q']
).properties(width=600, height=300)
st.altair_chart(chart4, use_container_width=True)

st.subheader("Observations on Wet Bulb VS Outlet:")
st.write("""To evaluate temperature at a distance from the air cooler source, we examined 
         Wet Bulb Temp VS Outlet Temperature. This approach aimed to avoid biased 
         evaluations by considering temperature changes closer to the source. Observations 
         indicated that both parameters, dry bulb temperature and wet bulb, decreased over time, 
         showing a synchronization with the cooler's outlet temperature. This alignment makes sense as 
         the temperature is directly dependent on the outlet temperature of the cooler.""")

st.subheader("Conclusion")
st.write("""Through repeated experiments, the results enabled our team to measure the 
         performance of our product, essential for maintaining its quality. Comparing
          our product's performance to established brands strengthens our claims about 
         its quality and effectiveness. The cooler proves effective at reducing temperature
          and improving humidity in our living space. All parameters, including the change 
         in outlet and inlet temperatures, contribute to a comprehensive understanding of 
         the product's performance.
""")
