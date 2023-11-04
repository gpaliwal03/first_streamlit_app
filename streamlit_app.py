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

streamlit.header("Fruityvice Fruit Advice_2")
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
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New Section to dispaly fruityvice api response
streamlit.header("Fruityvice Fruit Advice Fucntion calling")
try:
     fruit_choice_2 = streamlit.text_input('What fruit would you like information about...?')
     if not fruit_choice_2:
       streamlit.error("Please select a fruit to get information...")
     else:
       back_from_function = get_fruityvice_data(fruit_choice_2)
       streamlit.dataframe(back_from_function); 

except URLError as e:
    streamlit.error()
    

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

streamlit.header("The Fruit load list contains through function calling:")

def get_fruit_load_list():
    with my_cnx.cursor() as cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row_2 = get_fruit_load_list()
    streamlit.dataframe(my_data_row_2)



streamlit.header("All end user to add a fruit to the list  through function calling:")

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as cur:
         my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
         return "Thanks fo adding " + new_fruit
      
#Add a button to add fruit
add_my_fruit =  streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List..'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function_2 = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function_2)


streamlit.header("Lab Challenge: All end user to add a fruit to the list  through function calling:")

def insert_row_snowflake_Lab(new_fruit):
    with my_cnx.cursor() as cur:
         my_cur.execute("insert into FRUIT_LOAD_LIST values ('" + new_fruit +"')")
         return "Thanks fo adding " + new_fruit
      
#Add a button to add fruit
add_my_fruit_2 =  streamlit.text_input('Lab Work:What fruit would you like to add ?')
if streamlit.button('Lab work:Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function_3 = insert_row_snowflake_Lab(add_my_fruit_2)
    streamlit.text(back_from_function_3)


streamlit.header("View Our Fruit List-Add Your Favorites!")

#Add a button to load the fruit
if streamlit.button('Get Fruit Load List:'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row_3 = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_row_3)


streamlit.stop()
streamlit.header("Second Text Entry!")
add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
#streamlit.text("Thanks for adding jackfruit")
streamlit.write('Thanks for adding',add_my_fruit)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
