# st="alaga annaanaannana"
# # st=st.replace(" ","")
# threshold=len(st)//2
# for i in range(0,len(st)):
#     count=0
#     for j in range(0,len(st)):
#         if st[i]==st[j]:
#             count+=1
#     if count>=threshold:
#         print(i,end=" ")
# occurences_ele={}
# def occurences(li):
    
#     for ele in li:
#         if ele in occurences_ele:
#             occurences_ele[ele]+=1
#         else:
#             occurences_ele[ele]=1
 
# li=[1,3,2,3,3,3,4,3,4,3,5,5,3,5,5]
# occurences(li)

# print(occurences_ele.items())
# for ele,occ in occurences_ele.items():
#     if occ>=len(li)//2:
#         print(ele)
#         print(li.index(ele,len(li)),occ)

# Example list
arr = [10, 20, 30, 40, 30, 50]

# Find index of all occurrences of element 30
indices = [i for i,x in enumerate(arr) if x == 30]
print(f"Indices of element 30: {indices}")  # Output: Indices of element 30: [2, 4]
