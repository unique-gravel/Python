try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divided be zero")