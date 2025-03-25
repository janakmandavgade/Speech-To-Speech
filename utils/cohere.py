import cohere
import os
from dotenv import load_dotenv

load_dotenv()

COHERE_TOKEN = os.environ.get("COHERE_TOKEN")

co = cohere.Client(COHERE_TOKEN) 

def querycohere(ans):
    response = co.chat( 
        model='command',
        message=ans,
        temperature=0.3,
        chat_history=[],
        prompt_truncation='AUTO',
        # stream=True,
        citation_quality='accurate',
        connectors=[{"id":"web-search"}],
        documents=[]
    ) 
    print(response.text)
    return response.text