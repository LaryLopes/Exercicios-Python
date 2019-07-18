n = int(input("Digite um numero: "))
r = n%3
r2 = n%5

if r == 0 and r2 == 0:
    print ("FizzBuzz")
else:
    print(n)
