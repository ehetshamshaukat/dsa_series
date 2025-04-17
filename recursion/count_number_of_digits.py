def num_of_digit(n):
  if n <= 10:
    return 1
  short_ans=int(n/10)  
  ans=num_of_digit(short_ans)
  real_ans = 1 + ans
  return real_ans


num_of_digit(54321)
