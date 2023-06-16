word = input()

snake_case = ''
for char in word:
    if char.islower():
        snake_case += char
    else:
        snake_case += '_' + char.lower()

print(snake_case)