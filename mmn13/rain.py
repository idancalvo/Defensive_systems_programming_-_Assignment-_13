Rainfull_mi = "45, 65, 70.4, 82.6, 20.1, 90.8, 76.1, 30.92, 46.8, 67.1, 79.9"
list_Rainfull_mi =  Rainfull_mi.split(',')
num_rainy_months = 0
for x in list_Rainfull_mi:
    try:
        if float(x)>75 :
            num_rainy_months += 1
    except:
        print (x + " is not A number")
print(f"The number of rainy days: {num_rainy_months}")