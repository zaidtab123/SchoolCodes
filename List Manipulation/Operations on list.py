x=[16,11,29,36,51,34,69,3,13,19,27]
l=len(x)
l1=x[1:9]
l2=x[-1:-l-1:-2]
l3=l2+l1
len3=len(l3)
sum1=0

print("i) Concatenation:", l3)

print("\nii) Repetition:",l1*10)

for i in range(len3):
    sum1+=l3[i]
    
print("\niii) Sum of elements of L1 and L2=",sum1)