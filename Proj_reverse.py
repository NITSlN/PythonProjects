# Write a Python program that accepts a word from the user and reverse it.

a = input('Enter a word to reverse it:\n')
list = list(a)
# print(list)
lenght = len(a)
kaddu =[]
for i in range(0,lenght):
    kaddu.append(list[lenght-i-1])
print(''.join(kaddu))
