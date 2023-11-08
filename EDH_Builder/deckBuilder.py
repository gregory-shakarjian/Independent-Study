from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.memory import ChatMessageHistory

import os
os.environ['OPENAI_API_KEY'] = ''
api_key = os.getenv('OPENAI_API_KEY')

def get_data():
    loader = CSVLoader(file_path='./data/cards.csv')
    cards = loader.load()

    card_name = 'Lightning Bolt'
    if card_name in cards['data']:
        card_info = cards['data'][card_name]
        print(f'Card Name: {card_info["name"]}')

def get_rulings():
    history = ChatMessageHistory()

    system_template="You are an expert on the rules of Magic the Gathering"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    human_template="What are the rules for the Magic the Gathering game mode Commander?"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    request = chat_prompt.format_prompt().to_messages()
    
    chat = ChatOpenAI(openai_api_key=api_key)
    result = chat(request)

    history.add_ai_message(result.content)
    print(history.messages)

if __name__ == "__main__":
    get_rulings()
