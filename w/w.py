import os
os.chdir('d:/py')
a=os.listdir('d:/py')
file1=open(a[0],'r')
lines=file1.readlines()
i=1

for line in lines:
    i=i+1
    if line[0]=='n' and line[1]=='m':
        print i



file1.close()

r'test w'

