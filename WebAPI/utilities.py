from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
from torch import cuda
from _models import Query
device = 'cuda' if cuda.is_available() else 'cpu'

### Loading Llama 2 models
# llama2_model_name = 'meta-llama/Llama-2-7b-chat-hf'
# llama2_tokenizer = AutoTokenizer.from_pretrained(llama2_model_name)
# llama2_model = AutoModelForSeq2SeqLM.from_pretrained(llama2_model_name)

model_name = "google/pegasus-multi_news"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_book_name_t5_large (query:str):
    input_text = f"Generate Research Book name on {query}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
    outputs = model.generate(input_ids)
    return(tokenizer.decode(outputs[0]))
    
def generate_facts_t5_large(query:str):
    input_text = f"Give few information about {query}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
    outputs = model.generate(input_ids)
    return(tokenizer.decode(outputs[0]))

def generate_book_name_llama2_7b (query:str):
    input_text = f"Generate Research 10 Book name on {query}"
    input_ids = llama2_model_name(input_text,
                          return_tensors="pt").input_ids.to(device)
    outputs = llama2_model.generate(input_ids)
    return(llama2_tokenizer.decode(outputs[0]))
    
def generate_facts_llama2_7b(query:str):
    input_text = f"Give few information about {query}"
    input_ids = llama2_model_name(input_text,
                          return_tensors="pt").input_ids.to(device)
    outputs = model.generate(input_ids)
    return(tokenizer.decode(outputs[0]))