from fastapi  import FastAPI # Importing FastAPI for creating the web application, apis and models
from pydantic import BaseModel # Importing BaseModel from Pydantic for data validation and serialization
from typing import List # Importing List from typing for type hinting of lists

app = FastAPI() # Creating an instance of FastAPI

class Tea(BaseModel): # Defining a Pydantic model for Tea
    id: int
    name: str 
    origin: str

teas: List[Tea] = [] # Initializing an empty list to store tea objects

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return {"message": "Tea added successfully!", "tea": tea}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return {"message": "Tea updated successfully!", "tea": updated_tea}
    return {"message": "Tea not found!"}     

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            # del teas[index]
            deleted_tea = teas.pop(index)
            return {"message": "Tea deleted successfully!", "tea": deleted_tea}
    return {"message": "Tea not found!"}
