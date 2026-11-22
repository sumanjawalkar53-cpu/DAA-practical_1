n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
n = len(arr)
for i in range(n-1):
  min  = i
  for j in range(i+1,n):
    if(arr[j]< arr[min]):
      min = j
  if(min != i):
    arr[i],arr[min]=arr[min],arr[i]
print("Sorted array:",arr)

