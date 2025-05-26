from fastapi import FastAPI
from pydantic import BaseModel


class UserInput(BaseModel):
    name_1 : str
    name_2 : str

app = FastAPI()



def calculate_flames(get_name_1, get_name_2):
    name_1 = [char for char in get_name_1 if char != ' ']
    name_2 = [char for char in get_name_2 if char != ' ']

    total_length = len(name_1) + len(name_2)

    for word in name_1:
        if word in name_2:
            total_length -= 2
            name_2.remove(word)
            
    flames = list('flames')*100
    lookups = {'f':'are Friends','l':'are in Love','a':'both are having Affection','m':'will end up in Marriage','e':'are Enemies','s':'are Siblings'}

    value = total_length - 1

    for i in range(6):
        if len(set(flames)) == 1:
            break
        redu_list = [i for i in flames if i!= flames[value]]
        next_word = flames[value+1]
        flames = redu_list
        next_index = flames.index(next_word)
        value = next_index + (total_length - 1)
        
    destination = redu_list[0]

    return f"{get_name_1.title()} and {get_name_2.title()} {lookups[destination]}"


@app.post("/calculate_flames")
def calcuate(input: UserInput):

    result = calculate_flames(input.name_1, input.name_2)

    return result