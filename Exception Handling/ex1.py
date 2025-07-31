# Exception =  AN event that interrupts the flow of a program
#         (ZeroDivisionError, TypeError,ValueError)
#           1. try, 2.except, 3.finally

try:
    num = int(input("Enter a number: "))
    print(1/num)
    #num = num+"oops"
    #print(num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter Only number!")
except Exception:
    print("oops.. Something Went Wrong!")
finally:
    print("Do Some Clean up here!")