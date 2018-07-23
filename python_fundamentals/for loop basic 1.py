#1. Basic - Print all the numbers/integers from 0 to 150.
for x in range (0,151):
    print(x)

#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for x in range (5,1000000):
    if(x % 5 ==0):
        print(x)

#3. Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for x in range (1,100):
    if (x % 5 == 0):
        print("Coding")
    elif (x % 5 != 0 )
        print()

#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range (0,500000):
    if (i % 2 !=0):
        sum +=i
    print(sum)

#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
for i in range(2018, 1, -4):
    print(i)

#6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
for i in range (2,9,3):
    i+=1
    if i%3 ==0:
        print(i)