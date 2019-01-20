input = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = input.split(' ')
array = (1, 5, 6, 7, 8, 9, 15, 16, 19)
dic = {}

count = 0

for word in words:
    count += 1
    tmp = ""
    if count in array:
        tmp = word[:1]
    else:
        tmp = word[:2]
    dic[tmp] = count

print(dic)
