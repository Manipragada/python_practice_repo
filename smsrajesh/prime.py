
# Approach - 1:

# def Prime_number(num):
#     c=0
#     if num==1:
#         print(f"{num} is neither prime nor composite")
#     else:
#         for i in range(1,num+1):
#             if num%i==0:
#                 c+=1
#         if c==2:
#             print(f"{num} is Prime_Number")
#         else:
#             print(f"{num} is not a Prime_Number")


# Prime_number(int(input("Enter the Number : ")))



# Approach - 2:


def Prime_Checker(n):
    c=0
    if n%2==0:
        if n!=2:
            print(f"{n} is not a Prime_Number")
        else:
            print(f"{n} is a Prime_Number")
    else:
        for i in range(3,(n//2)+1,2):
            if n%i==0:
                c+=1
                if(c==1):
                    break
        if c==0:
            print(f"{n} is a Prime_Number")
        else:
            print(f"{n} is not a Prime_Number")

number=int(input("Enter the Number : "))
if(number == 0 or number == 1 or number < 0):
    print(f"{number} is not prime_Number")
else:
    Prime_Checker(number)







    

    