a=int(input("enter a number"))
b=a%2
if b==0:
  print("even",end='')
elif(a<0):
  print("invalid",end='')
else:
  print("odd",end='')
