def countingSort(arr):
    # Write your code here
    freq = [0]*100
    for i in range(0,len(arr)):
        freq[arr[i]] += 1
        
    return freq 
