
# a=123456.e5 #e5 represents no.of zeros
# print(a)

# a='foo bar'
# print(type(a))

# bubble sort
# li=[2,4,1,3,5,8,7]
# flag=1
# for i in range(len(li)-1):
#     for j in range(i+1,len(li)):
#         if(li[i]>li[j]):
#             li[i],li[j] = li[j],li[i]
#             flag=0
#     if(flag==1):
#         break

# print(li)

#tuples
# tup=("hello world", "world")
# tup1=tuple([1,2,3,4])
# print(tup1)
# print(type(tup1))

#dictionary

# dic={"india":"delhi",
#      "tamil-nadu":"chennai",
#      "kerala":"tiruvendrum",
#      "karnataka":"banglore"}
# for city in dic.keys():
#     print("{} is a capital of {}".format(dic[city], city))

#set maintain order in given list
# se={"durai"}
# se.add("alagu")
# print(se)

list=[2,1,3,6,5,9,10,4]
maximum=list[0]
for i in range(1,len(list)):
    if(maximum<list[i]):
        maximum=list[i]
print(maximum)

