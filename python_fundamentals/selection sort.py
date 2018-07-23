
array = [1,45,10,35,100,13,147,500,80]
size = len(array)


for i in range(0,size):
    for j in range(i+1,size):
        if array[j] < array[i]:
            min = array[j];
            array[j] = array[i];
            array[i] = min;



print(array)