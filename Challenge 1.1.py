def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
number =int(input ("Enter a value: ")
res=fact_rec(number )
prpint (" the factorial of{}is{}".format (numbers,res))