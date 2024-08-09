str1=input("enter the string1: ")
str2=input("enter the string2: ")
sorted_string1=sorted(str1)
sorted_string2=sorted(str2)

if(len(str1)==len(str2)):
    if(sorted_string1==sorted_string2):
        print("given string is anagram")
    else:
        print("given string is not anagram")