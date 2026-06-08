# sum of odd numbers from 1-10
sum=0
for i in range(1,11):
    if i%2!=0:  #i%2==1
        sum=sum+i
print("Sum = ",sum)