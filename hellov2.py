#First name
first_name=input("Enter your firstname! ")
#Last Name
last_name=input("Enter your lastname! ")
#Age
age=int(input("Enter your age!"))

height=float(input("Enter your height!"))

#Final Greeting
print(f"Hello {first_name} {last_name}! Your age is {age}!")

print(type(first_name))
print(type(last_name))
print(age + 51)
print(f'{(height + 0.1):.2f}')