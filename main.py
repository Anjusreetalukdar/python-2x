A,B = raw_input().strip().split(' ')
A,B = [str(A),str(B)]
a1=sorted(A)
b1=sorted(B)
if a1 <> b1:
  print("ERROR")