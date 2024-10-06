def create_tuples(list1, list2):
    return [(list1[i], list2[i]) for i in range(len(list2))]

input_str1 = input("Please Enter the list of numbers separated by spaces: ")
list1 = [int(x) for x in input_str1.split()]
list2 = []

for i in range(len(list1)):
    name = input(f"Please Enter a name for the number {list1[i]}: ")
    list2.append(name)

result = create_tuples(list1, list2)
print(f"Result: {result}")
