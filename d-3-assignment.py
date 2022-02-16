""" 
Difference between nested and chained conditionals--
    i. Nested conditionals have one or more conditionals inside it. Chained conditionals don't have any conditionals inside it. 
    sometimes nested conditionals can contain another nested conditional inside it.

    ii. Nested conditional are chellening to read and understand. On the other hand, chained conditionals are easier to read and understand. 


 """



#nested conditionals
#taking temperature from the user.
temperature = float(input("Enter your body temperature in Furenheit: ")) 

#applying nested conditions to show fever informations.
if 98.5<temperature<110:
    if 98.6<=temperature<=100:
        print("You've normal fever!")
    elif 100<temperature<=102:
        print("You've medium level fever! ")
    elif 102<temperature<=103:
        print("You've high level fever!")
    else :
        print("You've extreme level fever!")

elif temperature>110:
        print("You've entered a wrong temperature")
elif temperature<90:
    print("Your body is loosing it's tempeture!")
else: 
    print("You are absolutely healthy!")



""" 
output-

Enter your body temperature in Furenheit: 99
You've normal fever!

The output will be different for differnt user input
Fisrt it will tell the user to input temperature suppose the user entered 99.
The the output will show according to the input.
Note- both of the conditionals will show same result for the same input.
 """

"""
The strategy to avoid nested conditional can be different for every nested conditonals. In the example below I just brought the conditionals out and added more elif statements to avoid nested conditionals. In genaral, we can use 'and' or 'or' operator to avoid nested conditionals, or we can use more elif statements. 

 """

#chained conditionals
#taking temperature from the user.
temperature = float(input("Enter your body temperature in Furenheit: "))

#applying chainded conditionals for the same problem above
if temperature<90:
    print("Your body is loosing it's temperature!")
elif 98.6<=temperature<=100:
    print("You've normal fever!")
elif 100<temperature<=102:
    print("You've medium level fever!")
elif 102<temperature<=103:
    print("You've high level fever!")
elif 110>temperature>103:
    print("You've extreme level fever!")
elif temperature>110:
    print("You've entered a wrong temperature!")
else :
    print("You are absolutely healthy!")

""" 
output-

Enter your body temperature in Furenheit: 112
You've entered a wrong temperature!

The output will be different for differnt user input
Fisrt it will tell the user to input temperature suppose the user entered 112.
The the output will show according to the input.
Note- both of the conditionals will show same result for the same input.
 """

    