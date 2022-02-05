def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


n = int(input("enter the no. of test cases you want to check"))

lst = []
sum = []

for i in range(n):
  x = int(input("input your value:"))
  lst.append(x)

for item in lst:
  x = [int(a) for a in str(item)]
  res = []
  for i in x:
      res.append(pow(i, len(x)))
      Sum  =sum_list(res)

  if(item == Sum):
     print("It is an ARMSTRONG number")

  else:
    print("It is NOT an ARMSTRONG number")