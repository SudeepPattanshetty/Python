a = eval(input("Enter the first number: "))
b = eval(input("Enter the second number: "))
c = eval(input("Enter the third number: "))

if(a>b):
  if(a>c):
    if(b>c):
      h = a
      l = c
    else:
      h = a
      l = b
  else:
    h = c
    l = b
elif(a>c):
  h = b
  l = c
elif(b>c):
  h = b
  l = a
else:
  h = c
  l = a

print("Highest Value is: ",h)
print("Lowest Value is: ",l)
