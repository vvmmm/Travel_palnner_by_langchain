#LOGIC 1 : chat_prompt_template
from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template= ChatPromptTemplate(
    messages=[("system","You act As a helpful AI Assistant for a travel agency. which help to find the flight, railway or bus bookings from source to destination. also give list of all available plan for travel in the form of table by mentioning all required details about the trip cost and facilities and etc."),
              ("human","Book a flight from {source} to {destination}.On date {date} .Have {passengers} no. of passengers. Dont ask any more informations. just give list of all available flights,railways and bus.")],
    partial_variables={"source":"ABD","destination":"HYB","passengers":1}
)



#LOGIC 2 : chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

chat_model=ChatGoogleGenerativeAI(google_api_key="AIzaSyC1B3zDW4G19olwgTz368YgS-ZARqzsEFE",model="gemini-2.0-flash-exp",temperature=1)


# LOGIC 3 : output_parsers

from langchain_core.output_parsers import StrOutputParser

parser= StrOutputParser()

#LOGIC 4: chain
chain = chat_prompt_template | chat_model | parser

#LOGIC 5: ASK to user for input

import streamlit as st

st.title(":tophat: Mehta Travel Planner ~~")
source=st.text_area(label="Source:",placeholder="Enter Your Source...")
destination=st.text_area(label="Destination:",placeholder="Enter Your Destination...")
date=st.text_area(label="Date:",placeholder="Enter Your Journey Destination...")
passengers=st.text_area(label="No. Of Passengers:",placeholder="Enter No. Of Passengers...")

btn_click=st.button("Find A Trip Plan Availibility")
raw_input={"source":source,"destination":destination,"date":date,"passengers":passengers}
if btn_click==True:
    st.write(chain.invoke(raw_input))
    