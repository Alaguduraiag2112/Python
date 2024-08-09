day=int(input("enter the day: "))
month=int(input("enter the month: "))
year=int(input("enter the year: "))
max_days=0

def func(month,year):
        if(month==1 | month==3 | month==5 | month==7 | month==8 | month==10 | month==12):
            max_days=31
        elif(month==4 | month==6 | month==9 |month==11):
            max_days=30
        elif(year%4==0 and year%100!=0 or year%400==0):
            max_days=29
        else:
            max_days=28
        return max_days
max_days=func(month,year)
print(max_days)
if(day<0 or day>max_days):
     print("date is invalid")
elif(month<0 or month>12):
     print("date is invalid")
else:
     print("given date is valid")

