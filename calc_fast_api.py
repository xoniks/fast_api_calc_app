from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculationInput(BaseModel):
    operation: str 
    num1: float 
    num2: float
    
class CalculationOutput(BaseModel):
    operation: str
    num1: float
    num2: float
    result: float
    

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        return None
    
@app.post("/calculate", response_model=CalculationOutput)
async def calculate(calculation: CalculationInput):
    
    if calculation.operation =='1':
        result = add(calculation.num1,calculation.num2)
    
    elif calculation.operation =='2':
        result = subtract(calculation.num1,calculation.num2)
    
    elif calculation.operation =='3':
        result = multiply(calculation.num1,calculation.num2)
        
    elif calculation.operation =='4':
        if calculation.num2 == 0:
            return {'detail': 'Error! Division by zero!'}
        else:
            result = divide(calculation.num1,calculation.num2)
            
    else:
        return {'detail': 'Invalid opeartion.'}
    
    return {
        'operation': calculation.operation,
        'num1': calculation.num1,
        'num2': calculation.num2,
        'result': result
    }