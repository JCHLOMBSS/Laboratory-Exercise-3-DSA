def vowelsToUpper(s):
    vowels = 'aeiou'
    return ''.join([char.upper() if char in vowels else char for char in s])

while True:
    sentence = input("Enter a short word or sentence (or type 'no' to stop): ")
    if sentence.lower() == 'no':
        break
    print(vowelsToUpper(sentence))
