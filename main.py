import requests
import sqlite3
import streamlit as st
import pandas as pd
import numpy as np
from random import randint

#create multiple pages
st.sidebar.success("Next Page from here")

#filtering cat data function
def filter_cat_data(df,name,origin,weight_range,life_range):
    #filter by name,origin,weight and life
    if name:
        df = df[df['name']==name]
    if origin:
        df = df[df['origin']==origin]
    df = df[df['max_weight'].between(weight_range[0],weight_range[1])]
    df = df[df['max_life_expectancy'].between(life_range[0],life_range[1])] 
    print(df['image_link'])
    #generate kitty pictures
    st.image(df['image_link'].iat[0])
    
    return df

#filter breeder information function, filering by name and rating.
def filter_breeder_data(df,name,rating):

    if name:
        df = df[df['name']==name]
    df = df[df['rating'].between(rating[0],rating[1])]
    return df

#read the data from database
conn = sqlite3.connect("Cat.sqlite")

#create panda dataframe
df_CAT = pd.read_sql('SELECT * FROM CATS', conn)
df_BREEDER = pd.read_sql('SELECT * FROM BREEDERS',conn)

conn.close()

#read data from txt file.
df_facts = open('CATFACTS.txt')
facts = df_facts.readlines()


#create titile and author information and simple explanation.
st.title("This is the Cat Data and Breeder Selection APP")
st.markdown( '''Select Your interested Kitty Breed')
                Find your dream breeder in Los Angeles area')
                Author: Tianyu Wang''')

#create filtering tag and tool
cat_name = st.sidebar.text_input("Cat Breed")
origin = st.sidebar.text_input('Origin Country')
weight_range = st.sidebar.slider("Weight range", 0, 20, (0, 20))
life_range = st.sidebar.slider("Life Range", 0, 20, (0, 20))

#run the filtering functions and write and resulting and pictures.
if st.sidebar.button("Submit Cat"):
    st.write(filter_cat_data(df_CAT,cat_name,origin,weight_range,life_range))
    #make some cold knowledge about kitty
    st.write(":red['Hey!Little Tips!']",(facts[randint(0,49)].strip()))
else:
    st.write(df_BREEDER)
    st.write(df_CAT)
    st.write(":red['Hey!Little Tips!']",(facts[randint(0,49)].strip()))


#filtering breeder information
breeder_name = st.sidebar.text_input("Breeder Name")
rating = st.sidebar.slider("Rating range", 0, 5, (0, 5))

#run filering function
if st.sidebar.button("Submit Breeder"):
    st.write(filter_breeder_data(df_BREEDER,breeder_name,rating))
    st.write(":red['Hey!Little Tips!']",(facts[randint(0,49)].strip()))
