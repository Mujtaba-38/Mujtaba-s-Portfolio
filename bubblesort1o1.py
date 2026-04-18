x = "==================="
y = "      Welcome      "

print(x)
print(y)
print(x)

print("today we are going to build a stack for the first time. ")

TheStack= [1,3,5,7,8,45,23,56,78,98,87,233,546,675]
Pass = 1
Swap = False
while Pass < len(TheStack)-1 and Swap == False:
    for index in range(1, len(TheStack)-1):
     if TheStack[index] > TheStack[index+1]:
        temp = TheStack[index]
        TheStack[index]= TheStack[index+1]
        TheStack[index+1] = temp
        Swap = True
    Pass = Pass +1

for i in range(1, len(TheStack)):
   print(TheStack[i])




 


