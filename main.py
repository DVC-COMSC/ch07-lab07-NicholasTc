numbers = input().split()
evenlist = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for y in range(len(numbers) - 1, -1, -1):
    if y % 2 == 0:
        evenlist.append(numbers.pop(y))

# for n in numbers:
#     if n in evenlist:
#         numbers.remove(n)

evenlist.reverse()
print("The list numbers \n", numbers)
print("The list for even index elements\n", evenlist)
