
import streamlit


streamlit.header('New Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_first_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_first_list = my_first_list.set_index('Fruit')
#Let's put a [ick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_first_list.index))

#display the table on the page
streamlit.dataframe(my_first_list)

