#Program to check if the alphabet is vowel or constant 


alphabet = input("Enter the alphabet:")
if alphabet.lower() in  "aeiou" :
    print("The given alphabet is a vowel")
else:
    print("The given alphabet is a consonant")
