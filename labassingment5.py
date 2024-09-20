# Aim:

# Write a python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using

# a) Insertion sort

# b) Shell Sort and display top five scores

n=int(input("Enter Number Of SE Students :"))

def input_marks():
    marks=[]
    for i in range(n):
        marks.append(float(input("Enter Marks Of SE Students {0} :".format(i+1))))
    return marks

def display_marks(marks):
    for i in range(len(marks)):
            print("Marks of Student {0}:".format(i + 1),marks[i])

def insertion_sort(marks):
    for i in range(1, len(marks)):
        val = marks[i]
        j = i - 1
        while j >= 0 and marks[j] > val:
            marks[j + 1] =marks[j]
            j -= 1
        marks[j + 1] = val
    return marks


def shell_sort(marks):
    n = len(marks)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = marks[i]
            j = i
            while j >= gap and marks[j - gap] > temp:
                marks[j] = marks[j - gap]
                j -= gap
            marks[j] = temp
        gap //= 2
    return marks

def top_five(marks):
    if (len(marks)<5):
          start,end=len(marks)-1,-1
    else:
        start,end=len(marks)-1,len(marks)-6
    
    for i in range(start,end,-1):
        print(marks[i])

a=input_marks()
display_marks(a)
print("insertion sort :",insertion_sort(a))
print("shell sort :",shell_sort(a))
top_five(a)
