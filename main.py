
# ******************************
# Make your Code
# ******************************
numbers = input().split()
evenlist = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for y in range(len(numbers)):
    if y % 2 == 0:
        evenlist.append(numbers[y])

for n in numbers:
    if n in evenlist:
        numbers.remove(n)

print("The list numbers \n", numbers)
print("The list for even index elements\n", evenlist)
