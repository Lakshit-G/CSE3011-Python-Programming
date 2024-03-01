# program to enter numbers till the user wants and at the end display largest and smallest numbers entered
largest = None
smallest = None

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print(f"Largest number entered is {largest}")
print(f"Smallest number entered is {smallest}")
