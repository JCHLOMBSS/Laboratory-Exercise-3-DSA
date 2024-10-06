def create_tuples(list1, list2):
    return [(i+1, list2[i]) for i in range(len(list2))]

list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

result = create_tuples(list1, list2)
print(f"Result: {result}")
