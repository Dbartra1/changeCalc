##Dillon Bartram APS Week 2 Ex the remix to ignition##

print ("Change Calculator 9000" , '\n')

while True:
    
    c = int (input ("Enter number of cents: "))
    print ("\n")

    ##Starts largest coin first, use medulo operator to find remainder##
    print ("Quarters:", c//25)
    c = c % 25
    print ("Dimes:   ", c//10)
    c = c % 10
    print ("Nickles: ", c//5)
    c = c % 5
    print ("Pennies: ", c//1, '\n')

    res = input ("Continue (y/n): ")
    print ('\n')

    if res =='N' or res =='n':
        print ("Bye!!!!!")
        break

    
 
