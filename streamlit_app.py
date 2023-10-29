import streamlit 
import pandas
streamlit.title('MY Parents New Healthy Dinner')

#streamlit.header('Breakfast Menu')
#streamlit.text('Oatmeal,Apple,Juice')
#streamlit.text('Kale,Spinch')
#streamlit.text('Hard Boiled Egg ,Toast')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Oatmeal 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinch &   Rocket Smoothie')
streamlit.text(' 🐔  Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list =pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#Lets put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits :",list(my_fruit_list.index))

#Display teh table on the page
streamlit.dataframe(my_fruit_list)

