# ques={"question":"If x=8, then what is the value of 4(x+3) ?","A":35,"B":36,"C":40,"D":44}
# print("Answer the following algebra question: ")
# for key,value in ques.items():
#     print(key,value)
# answer=input("Your choice: ")
# if answer=="D":
#     print("Congrat !")
# else:
#     print("Oh-no,that wrong !")
# ------------------------------------------------------------------------------------------------

as1={"question":"If x=8, then what is the value of 4(x+3) ?","A":35,"B":36,"C":40,"D":44}
as2={"question":"Jack scores these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?","A":"About 55","B":"About 65","C":"About 75","D":"About 85"}
score=0
print("Answer the following algebra question: ")
button=input("Are u ready ? (yes-no) ")
if button == "yes":
    for key,value in as1.items():
        print(key,value)
    answer1=input("Your choice: ")
    if answer1=="D":
        print("Congrat !")
        score+=1
    for key,value in as2.items():
        print(key,value)
    answer2=input("Your choice: ")
    if answer2=="B":
        print("Congrat !, your test finished")
        score+=1
    print("you correctly answer ",score," out of 2 question")
elif button=="no":
    print("ok, good bye")



    