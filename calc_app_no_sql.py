from pymongo import MongoClient

def create_connections():
    client = MongoClient('localhost',27017)
    db = client['calculator_db']
    return db

def insert_calculation(db,calculation):
    collection = db['my_calculations']
    id = collection.insert_one(calculation).inserted_id
    return id


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
        return "Division with zero"
    
    
def calculator():
    print('Please select an operation:')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    
    db = create_connections()
    
        
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1','2','3','4'):
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            
            if choice == '1':
                result = add(num1,num2)
                print(num1,"+",num2,"=",add(num1,num2))
            
            elif choice == '2':
                result = subtract(num1,num2)
                print(num1,"-",num2,'=',subtract(num1,num2))
                
            elif choice == '3':
                result = multiply(num1, num2)
                print(num1,'*',num2,'=',multiply(num1,num2))
            
            elif choice == '4':
                result = divide(num1,num2)
                print(num1,'/',num2,'=',divide(num1,num2))
                
            calculation = {
                'operation':choice,
                'num1':num1,
                'num2':num2,
                'result':result,
            }
            insert_calculation(db, calculation)
            break
        else:
            print("Invalid input")
    
if __name__ == '__main__':
    calculator()
