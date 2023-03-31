string = input("Enter any word:")
total_vowels = 0
for vowels in string:
    string = str(vowels)
    if vowels in 'aeiouAEIOU':
        total_vowels+=1
print(total_vowels)        





