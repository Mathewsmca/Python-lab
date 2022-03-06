list1 = [1, -2, 3, -4, 5, 6, -7, 8, -9, 10]
print("list1 : ", list1)
print("Positive numbers : ")
for num in list1:
    if num >= 0:
        print(num)

list2 = [1, 2, 3, 4, 5, 34, 6, 78, 4, 8]
print("list1 : ", list2)
print("square of list1 : ")
for n in list2:
  print(n**2)

n = input("Enter a word : ")
vowels = ['a', 'e', 'i', 'o', 'u']
list1 = []
for x in n:
    if x in vowels and x not in list1:
        list1.append(x)
print("vowels from list are  :", list1)

a = input("Enter a word : ")
print("ordinal values : ")
list1 = []
for x in a:
    list1.append(ord(x))
print(list1)
