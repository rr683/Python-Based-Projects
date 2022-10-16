# pg 100 looping through all key value pairs

user_o = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_o.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'Edward': 'Ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}")

#Page 103
#sorting keys with keys as a default in a dictionary
for name in sorted(favorite_languages):
    print(f"{name}, thank you for taking the poll")