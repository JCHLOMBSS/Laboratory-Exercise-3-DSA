def get_squared_odds(input_list):
    return [x**2 for x in input_list if x % 2 != 0]

input_str = input("Please enter your numbers then separate it with spaces: ")
input_list = [int(x) for x in input_str.split()]

squared_odds = get_squared_odds(input_list)

print(f"Squared odds from {input_list}: {squared_odds}")
