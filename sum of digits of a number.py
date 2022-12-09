print("Enter your number ")
n=input()
sum=0
for i in range(0,len(n)):
    sum=sum+int(n[i])
print(f"sum of digits in number = {sum} ")
if sum%2 == 0:
 print("false")
else:
 print("true")