a = eval(input("Enter the first number: "))
b = eval(input("Enter the second number: "))
c = eval(input("Enter the third number: "))

if(a>=b and a>c and b>c):
  h = a
  l = c
elif(a>b and a>=c and c>b):
  h = a
  l = b
elif(b>=a and b>c and a>c):
  h = b
  l = c
elif(b>a and b>=c and c>a):
  h = b
  l = a
elif(c>=a and c>b and a>b):
  h = c
  l = b
elif(c>a and c>=b and b>a):
  h = c
  l = a

print("Highest Value is: ",h)
print("Lowest Value is: ",l)
