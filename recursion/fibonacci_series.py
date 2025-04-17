def fib_series(n):
  if n <= 0:
    return 1
  n1=fib_series(n-1)
  n2=fib_series(n-2)
  ans=n1+n2
  return ans

fib_series(5)
