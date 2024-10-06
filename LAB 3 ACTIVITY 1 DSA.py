def get_squared_odds(input_list):
    return [x**2 for x in input_list if x % 2 != 0]

sample_list1 = [2, 4, 3]
sample_list2 = [0, 0, 1, 1]

squared_odds1 = get_squared_odds(sample_list1)
squared_odds2 = get_squared_odds(sample_list2)

print(f"Squared odds from {sample_list1} {squared_odds1}")
print(f"Squared odds from {sample_list2} {squared_odds2}")