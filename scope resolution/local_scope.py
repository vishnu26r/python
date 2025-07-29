
#this is a local scope , we can access only within the function 
def func1():
    a=1
    print(a)

def func2():
    b=2
    print(b)
   # print(a) // can't do like this , calling variable from another function


func1()
func2()