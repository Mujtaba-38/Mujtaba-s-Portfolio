x = "==================="
y = "      Welcome      "

print(x)
print(y)
print(x)

print("today we are going to build a stack for the first time. ")

TheStack = [1, 3, 5, 7, 8, 45, 23, 56, 78, 98, 87, 233, 546, 675]
Pass = 0
n = len(TheStack)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if TheStack[j] > TheStack[j + 1]:
            # Swap elements
            temp = TheStack[j]
            TheStack[j] = TheStack[j + 1]
            TheStack[j + 1] = temp
            swapped = True
    if not swapped:
        break

print("\nSorted array:")
for i in range(len(TheStack)):
    print(TheStack[i])
