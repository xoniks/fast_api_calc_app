import sqlite3

def create_connection():
    conn=None
    try:
        conn = sqlite3.connect('calculator.db')
        print(sqlite3.version)
    except:
        print('Error')
    return conn

def create_table(conn):
    try:
        sql = '''
                CREATE TABLE Calculations (
                    id integer PRIMARY KEY,
                    operation text NOT NULL,
                    num1 real NOT NULL,
                    num2 real NOT NULL,
                    result real
                );
                '''
        conn.execute(sql)
    
    except:
        print("Error")
    
    
def inser_calculations(conn,calculation):
    sql = """
            INSERT INTO Calculations(operation,num1,num2,result)
            VALUES (?,?,?,?)
            """
    cur = conn.cursor()
    cur.execute(sql,calculation)
    return cur.lastrowid

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
    
    conn = create_connection()
    
    if conn is not None:
        
        create_table(conn)
        
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
                    
                calculation = (choice,num1,num2,result)
                inser_calculations(conn,calculation)
                conn.commit()
                break
            else:
                print("Invalid input")
        
if __name__ == '__main__':
    calculator()
        
        