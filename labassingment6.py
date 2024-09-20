# Aim:

# Write a python program to store first year percentage of students in array.
# Write function for sorting array of floating point numbers in ascending 
# order using quick sort and display top five scores.


n=int(input("Enter Number Of Students :"))

def input_marks():
    marks=[]
    for i in range(n):
        marks.append(float(input("Enter Marks Of Students {0} :".format(i+1))))
    return marks

def display_marks(marks):
    for i in range(len(marks)):
            print("Marks of Student {0}:".format(i + 1),marks[i])

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1        
    
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)



def top_five(marks):
    if len(marks)<5:
          start,end=len(marks)-1,-1
    else:
        start,end=len(marks)-1,len(marks)-6
    
    for i in range(start,end,-1):
        print(marks[i])



a=input_marks()
display_marks(a)
quicksort(a, 0, len(a) - 1)
print("Sorted Marks:", a)
top_five(a)

