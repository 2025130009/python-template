a=int(input())
tens = a // 10
ones = a % 10

if tens % 3 == 0 and ones % 3 == 0:
    print("**")
elif tens % 3 == 0 or ones % 3 == 0:
    print("??")
else:
    print(">>")
  
