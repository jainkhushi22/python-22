amt=int(input("enter amount"))
print("*"*50)
amt500=amt//500
amt=amt%500
print("\tno. of 500 rupees notes {} and remaining amount is {} ".format(amt500,amt))
amt200=amt//200
amt=amt%200
print("\tno. of 200 rupees notes {} and remaining amount is {} ".format(amt200,amt))
amt100=amt//100
amt=amt%100
print("\tno. of 100 rupees notes {} and remaining amount is {} ".format(amt100,amt))