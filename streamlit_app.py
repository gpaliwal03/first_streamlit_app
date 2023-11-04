import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

#Lets put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruit:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)


#pre-populate the list

fruits_selected = streamlit.multiselect("Pick some fruits :",list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)


#Filter the Table Data

fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page 
streamlit.dataframe(fruits_to_show)


#streamlit.header("Fruityvice Fruit Advice_1!")
#import requests
####fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
###streamlit.text(fruityvice_response.json()) #just write the on screen
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)


# putting below section of code in try else block
##streamlit.header("Fruityvice Fruit Advice!")
##fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
##streamlit.write('The user entered ', fruit_choice)
##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
##fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
##streamlit.dataframe(fruityvice_normalized)

streamlit.header("Fruityvice Fruit Advice!!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
  else:
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       streamlit.dataframe(fruityvice_normalized)

except URLError as e:
    streamlit.error()

streamlit.header("Function calling!")

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New Section to dispaly fruityvice api response
streamlit.header("Fruityvice Fruit Advice Fucntion calling")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
  else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(fruityvice_normalized); 





streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#3my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
##my_data_row = my_cur.fetchone()
###streamlit.text("Hello from Snowflake:")
##streamlit.text(my_data_row)

my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.text("The Fruit load list contains:")
#streamlit.text(my_data_row)
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_row)


streamlit.header("Second Text Entry!")
add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
#streamlit.text("Thanks for adding jackfruit")
streamlit.write('Thanks for adding',add_my_fruit)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
