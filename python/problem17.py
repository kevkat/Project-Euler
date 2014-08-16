import time
 
start = time.time()
 
ones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundreds = 7
thousands = 8
 
total = 0
for i in range(1,1000):
    c = i % 10 # ones digit
    b = ((i % 100) - c) / 10 # tens digit
    a = ((i % 1000) - (b * 10) - c) / 100 # hundreds digit
 
    if a != 0:
        total += ones[a] + hundreds # "ones[a] hundred
        if b != 0 or c != 0: total += 3 # add 3 for "and"
    if b == 0 or b == 1: total += ones[b * 10 + c]
    else: total += tens[b] + ones[c]
 
total += ones[1] + thousands
elapsed = time.time() - start
 
print "%s found in %s seconds" % (total,elapsed)