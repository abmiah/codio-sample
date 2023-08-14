def func():
    user_input: str = ""

    while True:
        if len(user_input) == 0:
            print("Please enter your name")
        else:
            user_input
            break
        user_input = str(input("Hello, what is you're name: "))   
        
    print(f"Hello {user_input}, welcome to Coido") 

func()