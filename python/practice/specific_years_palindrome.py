
year=int(input("enter the year: "))

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

for month in range(1,12+1):
    max_days=func(month,year)
    for day in range(1,max_days+1):
         dd=str(day)
         mm=str(month)
         yyyy=str(year)
         if(day<10):
              dd="0"+dd
         if(month<10):
              mm="0"+mm
         date=dd+mm+yyyy
         reversed=date[::-1]
         if(date==reversed):
              print(day,"/",month,"/",year) 