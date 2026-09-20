number = int(input("Give me a number: "))

# positive, negative or zero
if number > 0:
    result1 = "positive"
elif number < 0:
    result1 = "negative"
else:
    result1 = "zero"

#odd or even
if number %2 == 0:
    result2 = "even"
else:
    result2 = "odd"

#greater or less then 100
if number > 100:
    result3 = "biger than 100"
else:
    result3 = "smaller than 100"

print(f"Given number is, {result1}, {result2}, and {result3}")