def func():
    user_input: str = ""
    user_input_age: int = ""

    while True:
      if len(user_input) == 0:
        try:
          user_input = str(input("Hello, please enter your name > "))
          continue
        except ValueError:
          print("Error")     
      
      if user_input:
        try:
          user_input_age = int(input(f"Hello, {user_input.title()} how old are you? "))
          print(f"{user_input.title()} you are {user_input_age} years old, in dog years that would be {user_input_age + (15 + 9)*5}")
          break
        except:
           print("Please enter a valid age") 
    print("Welcome to MSc Cyber Security Course")
      

func()
# def func():
#     while True:
#         user_input = input("Hello, please enter your name > ").strip()
        
#         if not user_input:
#             print("Error")
#             continue

#         try:
#             user_input_age = int(input(f"Hello, {user_input.title()} how old are you? "))
#             dog_years_age = user_input_age + (15 + 9) * 5
#             print(f"{user_input.title()}, you are {user_input_age} years old, in dog years that would be {dog_years_age}")
#             break
#         except ValueError:
#             print("Please enter a valid age")

#     print("Welcome to MSc Cyber Security")

# func()