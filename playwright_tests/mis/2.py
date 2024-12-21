A = "my name is Chaitanya"
B = "my naam is Chaitanya ok"


#find
#name ok
#substitution naam,insertion ok,deletion

if(len(A)<len(B)):
    #print("New insertion happened in B")
    length=len(B)-len(A) #12-10=2
    print("the new insertion is",B[-length:])

# for i in range(0,len(A)):
#     if A[i]==B[i]:
#         continue
#     else:
#         print("At index i the character got substituted",B[i])
#         break
list_A=A.split(' ')
#print(list_A)
list_B=A.split(' ')
for word in list_B:
    if word not in list_A:
        print("substitution happened for",word)

