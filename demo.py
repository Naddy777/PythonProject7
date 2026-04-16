# import requests
# result = requests.get("http://www.google.com/")
# print(result.text)

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")

message = "Hello"

# for c in message:
#     print(c)
#
# for n in range(4, 10):
#     print(n, end=" ")

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
