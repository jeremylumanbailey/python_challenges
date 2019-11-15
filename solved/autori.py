# https://open.kattis.com/problems/autori

hello = input()
output = ""
for x in hello:
    if x.isupper():
        output = output + x
print(output)
