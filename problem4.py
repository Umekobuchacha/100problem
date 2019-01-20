input = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
tmp = input.split(' ')
list = []

for x in tmp:
    list.append(len(x))

print(list)
