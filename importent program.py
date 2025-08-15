a=[]
b=0
c=int(input('enter the number:'))
for i in range(1,c+1):
    d=int(input(f'\nEnter the number{i}:'))
    a.append(d)
    b+=a[0]

print('\nMarks on each subject:',a)
print('\nTotal marks:',b)
