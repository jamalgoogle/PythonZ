arr = [1,2,4,4]
for i in range(len(arr)):
   for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == 9:
         print(f'The pair of elements at indices {i} , its value is  {arr[i]} and {j} , and its value is{arr[j]} sum up to 9.')









