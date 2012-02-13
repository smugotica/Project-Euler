i = 0
sum = 0

while i < 1000:
    if i % 3 == 0:
        sum = i + sum
        i = i + 1
    elif i % 5 == 0:
        sum = i + sum
        i = i + 1
    else:
        i = i + 1
    print "The sum is now %d" % sum

print "The final sum is %d" % sum
