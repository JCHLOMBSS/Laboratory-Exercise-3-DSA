def vowelsToUpper(s):
    vowels = 'aeiou'
    return ''.join([char.upper() if char in vowels else char for char in s])

print(vowelsToUpper(""))
print(vowelsToUpper("Hello, world!"))
print(vowelsToUpper("hello hi bye"))