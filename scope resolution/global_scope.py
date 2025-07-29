#if we declare variable in global we access it anywhere in the program

def func1():
    print(x)

def func2():
    print(x)

x=5

func1()
func2()