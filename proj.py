import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dateutil
import time

k = pd.read_csv("details.csv")
Name_filter = st.selectbox("Select Name",pd.unique(k["Name"]))

st.title("Streamlit Dashboard")
st.write("HEre is your Data")
st.write(k)
st.write(k.describe())

fig = plt.figure(figsize = (19,10))
plt.bar(k["Name"],k["Maths"],color="red")
plt.xlabel("Name")
plt.ylabel("Maths")
plt.title("Bar Chart")
st.pyplot(fig)

st.title("Histogram in Streamlit")

histfig = plt.figure(figsize=(2,1))
plt.hist(k["Maths"],color="Green",histtype="bar",rwidth=0.5)
plt.title("Histogram")
st.pyplot(histfig)


st.title("Line Plot  in Streamlit")
l = plt.figure(figsize=(6,1))
plt.title("Line_Plot")
plt.plot(k['Name'],k["Maths"],color="Blue")
st.pyplot(l)

st.title("Pie Chart in Streamlit")
m = plt.figure(figsize=(5,5))
plt.title("Pie_Plot")
ex = [0.1,0.0,0.0,0.0]
plt.pie(k["Maths"],labels=k["Name"],explode=ex)
st.pyplot(m)

st.title("Box Plot  in streamlit")
n = plt.figure(figsize=(3,2))
plt.title("Box_Plot")
plt.boxplot(k["Maths"],vert=False,widths=0.1,showmeans=True,labels=["BOX_PLOT"],patch_artist=True,boxprops=dict(color="r"),whiskerprops=dict(color="blue"),capprops=dict(color="green"))
st.pyplot(n)

st.subheader('Subhead')
st.caption('caption')
st.button('Submit')
st.code('for x in a')
st.checkbox('Tearms and policy')
st.selectbox('Enter sub',['HTML','CSS','JS','PHP','PYT'])
if st.checkbox('acknowledge'):st.write('welcome')
if st.button('click to read this dataset'):st.table(k)
st.multiselect('Enter sub',['HTML','CSS','JS','PHP','PYT'])
st.balloons()
st.progress(10)
# with st.spinner('loading'):time.sleep(5)
# x = st.text_input('Enter your Name')
# st.write(x)
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')

