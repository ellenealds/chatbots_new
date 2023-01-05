import pandas as pd
import cohere
import streamlit as st
from conversant.prompt_chatbot import PromptChatbot
from conversant.prompts import ChatPrompt
from dataanalyst import new_data_analyst_config
from datascientist import data_scientist_config
import logging
logging.basicConfig(level=logging.DEBUG)
#API = st.secrets["api_secret"]

co = cohere .Client("b55ru767vjHE7IuQ0aaqQx9rIO3g7CN0zquVnEZY")


@st.experimental_singleton
def config_ds (data_scientist_config):
    co = cohere.Client("b55ru767vjHE7IuQ0aaqQx9rIO3g7CN0zquVnEZY")

    data_scientist_config = data_scientist_config

    data_scientist_bot = PromptChatbot(client=co, prompt=ChatPrompt.from_dict(data_scientist_config))
    
    return data_scientist_bot

# aet the session state
data_scientist_bot = config_ds(data_scientist_config)

@st.experimental_singleton
def config_da (new_data_analyst_config):
    co = cohere.Client("b55ru767vjHE7IuQ0aaqQx9rIO3g7CN0zquVnEZY")

    data_scientist_config = new_data_analyst_config

    data_scientist_bot = PromptChatbot(client=co, prompt=ChatPrompt.from_dict(data_scientist_config))
    
    return data_scientist_bot

# aet the session state
data_analyst_bot = config_da(new_data_analyst_config)

# Function that generates the response in the desired format
def generate_response(response):
    formatted_response = ''
    for i, item in enumerate(response):
        user = item['user']
        bot = item['bot']
        formatted_response += f'<div class="user-message">{user} 💬</div>\n'
        formatted_response += f'<div class="bot-message">{bot} 🤖</div>\n'
    return formatted_response

# Add pages to the sidebar, the side bar should be shown when the app is run
st.sidebar.title('Specialist Chatbots')
page = st.sidebar.selectbox('Who would you like to speak to?', ['Data Scientist Specialist', 'Data Analyst Specialist'])

#st.sidebar.title('Chat to a Specialist')
#page = st.sidebar.radio('Who would you like to speak to?', [ 'Data Scientist Specialist','Data Analyst Specialist'])

# add the home page
if page == 'Data Scientist Specialist':
    # Add a title to the page
    st.title('Data Scientist Specialist')
    # add a subheader explaining what the page is about
    st.subheader('Ask a question about any Data Science concepts')
    # this needs a chatbot interface
    # add a user input for the question
    question = st.text_input('Ask a question')
    # add a button to generate the answer
    if st.button('Submit'):
        # call the data_scientist_bot
        data_scientist_bot.reply(question)
        # get the response and set session state
        
        response = data_scientist_bot.chat_history
        # reverse the response so the most recent message is at the top
        response = response[::-1]
        # Generate the formatted response
        formatted_response = generate_response(response)

        # Add CSS styles
        st.markdown(
            f'''
            <style>
            .user-message {{
                background-color: #e6e6e6;
                border-radius: 16px;
                padding: 8px;
                margin: 8px 0;
                float: right;
                clear: both;
            }}
            .bot-message {{
                background-color: #e6e6e6;
                border-radius: 16px;
                padding: 8px;
                margin: 8px 0;
                float: left;
                clear: both;
            }}
            .chat {{
                border: 1px solid #cccccc;
                border-radius: 8px;
                overflow: hidden;
                width: 500px;
                margin: 0 auto;
                padding: 16px;
            }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

        # Display the response in the desired style
        st.markdown(
            f'<div class="chat">{formatted_response}</div>',
            unsafe_allow_html=True
        )



# add page for chatbot
elif page == 'Data Analyst Specialist':
    # Add a title to the page
    st.title('Data Analyst Specialist')
    # add a subheader explaining what the page is about
    st.subheader('Ask a question about any Data Analyst concepts')
    # this needs a chatbot interface
    # add a user input for the question
    question = st.text_input('Ask a question')
    # add a button to generate the answer
    if st.button('Submit'):
        # call the data_scientist_bot
        data_analyst_bot.reply(question)
        # get the response and set session state
        
        response = data_analyst_bot.chat_history
        # reverse the response so the most recent message is at the top
        response = response[::-1]
        # Generate the formatted response
        formatted_response = generate_response(response)

        # Add CSS styles
        st.markdown(
            f'''
            <style>
            .user-message {{
                background-color: #e6e6e6;
                border-radius: 16px;
                padding: 8px;
                margin: 8px 0;
                float: right;
                clear: both;
            }}
            .bot-message {{
                background-color: #e6e6e6;
                border-radius: 16px;
                padding: 8px;
                margin: 8px 0;
                float: left;
                clear: both;
            }}
            .chat {{
                border: 1px solid #cccccc;
                border-radius: 8px;
                overflow: hidden;
                width: 500px;
                margin: 0 auto;
                padding: 16px;
            }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

        # Display the response in the desired style
        st.markdown(
            f'<div class="chat">{formatted_response}</div>',
            unsafe_allow_html=True
        )





