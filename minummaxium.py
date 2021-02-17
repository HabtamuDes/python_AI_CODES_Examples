__author__ = 'warcraft'
largest = None
smallest = None
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
        print(num)

    if largest is None:
        largest = num
    if num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)





