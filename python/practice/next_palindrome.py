
day=int(input("enter the day: "))
month=int(input("enter the month: "))
year=int(input("enter the year: "))
max_days=0

def func(day,moth):
        if(month==1 | month==3 | month==5 | month==7 | month==8 | month==10 | month==12):
            max_days=31
        elif(month==4 | month==6 | month==9 |month==11):
            max_days=30
        elif(year%4==0 and year%100!=0 or year%400==0):
            max_days=29
        else:
            max_days=28
        return max_days

while True:
    max_days=func(day,month)
    if(day>0 and day<=max_days) and (month>0 and month<13):
        dd=""
        mm=""
        if(day<9):
            dd="0"+str(day)
        else:
            dd=str(day)
        if(month<9):
            mm="0"+str(month)
        else:
            mm=str(month)
        yyyy=str(year)
        date=dd+mm+yyyy
        if(date==date[::-1]):
            print(dd,"/",month,"/",year,"given date is palindrome")
            break
        else:
            day+=1
            if(day>max_days):
                day=1
                month+=1
                if(month>12):
                    month=1
                    year+=1

