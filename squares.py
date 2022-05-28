squares =[]
for values in range(1,11):
    square = values**2
    squares.append(square)
print(squares)

digits = list(range(0,10))

print(digits)
print(f" The minimum value: {min(digits)}")
print(f" The maximum value: {max(digits)}")
print(f" The sum: {sum(digits)}")

#Using List Comprehension
digits = [values ** 2 for values in range(1,20)]
print(digits)