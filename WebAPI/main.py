from typing import Dict
from _models import Query
from fastapi import FastAPI
from utilities import generate_book_name , generate_facts


app = FastAPI()


@app.get('/api/generate_book_name/{query}')
async def _generate_book_name(query:str):
    suggestions = generate_book_name(query)
    return {"message":suggestions}


@app.get('/api/generate_facts/{query}')
async def _generate_facts(query:str):
    facts = generate_facts(query)
    return {"message":facts}

