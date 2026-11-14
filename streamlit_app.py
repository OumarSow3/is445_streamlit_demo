# put streamlit code here as needed
import streamlit as st
import pandas as pd
import altair as alt

st.title = "UIUC main building inventory - Sow"

url_link = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"

df = pd.read_csv(url_link)


#print(df['Agency Name'].unique)

show_status = st.toggle("Color Bars by Current Status:")

df_agency = df.groupby(["Agency Name", "Bldg Status"]).size().reset_index(name='Buildings')

#print(df)

#print(df_agency)

print(df.columns.tolist())

chart_1 = alt.Chart(df_agency).mark_bar().encode(
    x=alt.X('sum(Buildings)'), y=alt.Y('Agency Name:N', sort="-x", axis = alt.Axis(labelLimit=0)),
    color=alt.Color("Bldg Status:N", title="Building Status", scale=alt.Scale(domain=["In Use", "In Progress", "Abandon"], range=["steelblue", 'yellow', 'red'])) if show_status else alt.value("steelblue"),
    tooltip=['Buildings', 'Agency Name', alt.Tooltip("sum(Buildings)")],).properties(
        title = '# Of Buildings per Agency', width = 1000, height=alt.Step(25))
    

#chart_1.show()
st.altair_chart(chart_1, use_container_width = False)

'''
For the first graph, I was mainly intterested in the different Agencies regarding teh buildings. The question I wanted to answer is: How many buildings does each Agency have, according to the dataset? To answer this question, I made a bar graph, with each row representing
a different agency, as seen through the dataset. This allowed me to directly compare roghly how some of the different agencies have a different number of buildings. The x-axis shows the numeber of buildings each Agency has, while the y-axis is for each agency.
To make it interactive, I allowed users to change the color of the graphs to show which ones are in use, which ones are being made, and which ones are considered abandoned. This allows for an interesting way to view the graphs while being interactive. I orded it with
the Agencies with the larges number of buildings on top, and having the building counts per agency descend from there to make the graph as legibile as possible, given the large number of agencies. For the status of the building, I kept steel blue to make it consistent
with the original graph, went with red for "abandoned" to contrast teh blue and went with yellow for in progreess, as a transtion between the other two colors. If I could add more to the graph, I would add counts for each of the bars in the graph, to help readers see
how many buildings each Agency has as opposed to just an estimation, especially since the bottom half of the graph can be much harder to read.
'''

#print(df.columns.tolist())

#print(df['Bldg Status'].unique())

st.header("Buildings by Year")

year_col = st.radio("Show by:", ['Year Constructed', 'Year Acquired'])

df_years = df[df[year_col] > 0]

df_years = df_years.groupby(year_col).size().reset_index(name='Count')

chart_2 = alt.Chart(df_years).mark_line().encode(
    x=alt.X(f"{year_col}:Q"), y=alt.Y("Count:Q"), tooltip = [year_col, 'Count']).properties(title = f"Number of Buildings by {year_col}", width=1000, height=400)

st.altair_chart(chart_2, use_container_width = False)

'''
For my second graph, I wanted to look at the different years presnt in the graph, and see how many buildings were made made each year. But since there was also the 'year aquired' column, I decided to let users switch between the two as anther opportunity for interactivity.
This resulted in the x-axis being the year and the y-axis being the number of buildings aquired or the number of buildings made in a given year. I tied to keep the graph as simple as possible, keeping the blue color for both and the given markers, and only increasig the size
to make seeing the graph a bit easier. Now that the graph has been made, I can see how similar the two graphs look in overall shape, and making the two graphs distinct colors would make reading the graph much easier. A second addition that would be intresting would be to add
a way to have both graphs present at the same time, with the two being different colors, to make comparing the two graphs easier.
'''
