#Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the #number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
countDown = 5
while (countDown >= 0):
    if countDown != 0:
        print(countDown)
        countDown = countDown - 1
    else:
        break


#Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
def prtRet(list):
    if len(list)>1:
        print(list[0])
        return(list[1])
print(prtRet([7,4]))


#First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
def firstpluslength(list):
    sum =len(list) + (list[0])
    return sum
print(firstpluslength([5,2,3,4]))


#Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that #are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function #return False
def valgreatsec(list):
    newlist = []
    if len(list)<2:
        return False
    elif len(list)>=2:
        for i in range (len(list)):
            if((list[i])>(list[1])):
                newlist.append(list[i])
        print(len(newlist))
    return newlist
print(valgreatsec([1,2,3,4,5,6,7,8]))


#This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This #function should take two numbers and return a list of length size containing only the number in value. For example, #lengthAndValue(4,7) should return [7,7,7,7].
def lenval(num1, num2):
    arr = []
    for i in range(0, num1, 1):
        arr.append(num2)
    return arr
print(lenval(3,4))
##need jinx