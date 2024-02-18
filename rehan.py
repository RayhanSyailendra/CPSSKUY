def factorial(n):
	if n == 0:
	return 1
   else:
   	return n * factorial(n - 1)
   	
number = 2
result = factorial(number)
print(f"bilangan faktorial dari {number} adalah {result}.")	
