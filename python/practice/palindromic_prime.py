num=int(input("enter the number: "))
reverse_num=int(str(num)[::-1])
if(num==reverse_num):
    print("palindrome number")

if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("this is not prime number")
            break
    else:
        print("this is  prime number",num)