n = int(input("Number : >>>"))

sum = 0

i = 0 

while 2*i+1 < n:
    odd = 2*i+1
    sum+=odd
    i+=1

print(f"sum : {sum}")