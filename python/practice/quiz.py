q1=""" "a"+"bc"=??
a.a
b.bc
c.bca
d.abc
"""
q2="""whic one of the floor division
a./
b.//
c.+
d.%
"""
q3="""whic one of the floor division
a./
b.//
c.+
d.%
"""
questions={q1:"d",q2:"a",q3:"c"}
print(questions.values())
name=input("enter your name: ")
score=0
print("welcome",name,"to quiz")
for i in questions:
    print(questions[i])
    ans=input("Enter your answer a/b/c/d: ")
    if(ans==questions[i]):
        print("you got the answer: ")
        score=score+1
    else:
        print("wrong answer: ")
        score-=1
print("final score:",score)
