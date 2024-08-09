def reverse(str):
    i,j=0,len(str)-1
    st=""
    for i in range(len(str)):
        st=str[i]+st
    print(st)
reverse("Alagudurai")
