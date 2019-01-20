input = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tmp = input.split(' ')
list = []

for word in tmp:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    list.append(count)

print(list)
