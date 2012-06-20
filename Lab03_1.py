# Solution 1
testValue=1
count=0
print "The first 50 prime numbers are"
while count<50:
    testValue += 1
    isPrime = True
    for j in range(2,int(testValue**0.5)+1):
        if testValue%j==0:
            isPrime = False
            break
    if isPrime:
        print testValue,
        if count%10==0:
            print
        count+=1

# Solution 2 Lab03_2a
for i in range(7):
    for j in range(1,i+1):
        print j,
    print
    
# Solution 2 Lab03_2b
for i in range(6,0,-1):
    for j in range(1,i+1):
        print j,
    print
    
# Solution 2 Lab03_2c
for i in range(7):
    for k in range(6-i,0,-1):
            print ' ',
    for j in range(i,0,-1):
        print j,
    print
    
# Solution 2 Lab03_2d
for i in range(6,0,-1):
    for j in range(1,i+1):
        print j,
    print
    for k in range(7-i):
            print ' ',

