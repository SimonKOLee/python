r"""
this is my exercise\n\n
"""
def c2f(c_value):
    if(c_value < -273):
        return "That temperature doesn't make sense!"
    else:
        return c_value*1.8 + 32

temps = [10,-20,-289,100]
with open("ex5.txt","w") as file:
    for temp in temps:
        result = c2f(float(temp))
        if "That temperature doesn't make sense!" != result:
            file.write(str(result)+"\n")
