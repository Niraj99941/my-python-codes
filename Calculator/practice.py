
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Cannot divide by zero"


print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)
print("Division:", div_result)

