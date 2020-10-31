def c2f(c_value):
    if(c_value < -273.15):
        return "That temperature doesn't make sense!"
    else:
        return c_value*1.8 + 32

temps = [10,-20,-289,100]
for temp in temps:
    print (c2f(float(temp)))
