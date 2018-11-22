temperature = [10, -20, -289, 100]

def writer(temperature):
    with open("temperatures.txt", "w") as myfile:
        for  t in temperature:
            if t > -273.15:
                f = t * 9/5 +32
                myfile.write("%s\n" %f)
            else:
                myfile.write("That temperature doesn't make sense!\n")


writer(temperature)
