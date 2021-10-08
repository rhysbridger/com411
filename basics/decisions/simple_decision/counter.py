odd_number=0
even_number=0

first_number=int(input("Please enter the first whole number."))
print(first_number)
second_number=int(input("Please enter the second whole number."))
print(second_number)
third_number=int(input("Please enter the third whole number."))
print(third_number)
print()

if first_number==(first_number % 2 != 0):
    odd_number= odd_number + 1
else:
    even_number= even_number + 1


if second_number==(second_number % 2 != 0):
    odd_number= odd_number + 1
else:
    even_number= even_number + 1


if third_number==(third_number % 2 != 0):
    odd_number= odd_number + 1
else:
    even_number= even_number + 1

print(f"There were {even_number} even and {odd_number} odd numbers.")