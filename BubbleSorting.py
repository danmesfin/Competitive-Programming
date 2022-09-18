def countSwaps(a):
    # Write your code here
    numSwap = 0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j] > a[j+1]:
                numSwap += 1
                a[j], a[j+1] = a[j+1], a[j] 
    print('Array is sorted in', numSwap, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1]) 
