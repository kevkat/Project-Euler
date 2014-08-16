#!/usr/bin/python
def collatz(n):
    max=(0,0)
    cache={}
    for i in range(1,n):
        key_label=str(i)
        counter=1
        while i!=1:
            if i%2==0:
                i=i/2
                counter+=1
                if str(i) in cache:
                    counter+=cache[str(i)]-1
                    break
            elif i%2!=0:
                i=(3*i)+1
                counter+=1
        cache[key_label]=counter
        if cache[key_label]>max[0]:
            max=(cache[key_label],int(key_label))
    return max

print(collatz(1000000))
