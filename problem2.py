str1 = "パトカー"
str2 = "タクシー"
output = ""

for (a, b) in zip(str1, str2):
    output += a
    output += b

print(output)
