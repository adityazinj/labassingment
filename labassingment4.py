# Aim:

# Write a python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using

# a) Selection Sort

# b) Bubble sort and display top five scores.

n=int(input("Enter The Number Of Sudents :"))
def input_percentage():
    perc=[]
    for i in range(n):
        perc.append(float(input("Enter The Percetage Of Students {0}:".format(i+1))))
    return perc

def display_percentage(perc):
    for i in range(len(perc)):
            print("perc of Student {0}:".format(i + 1),perc[i])

def selection_sort(perc):
    for i in range(0,len(perc)):
        for j in range(i+1,len(perc)):
            if perc[j]<perc[i]:
                  temp=perc[j]
                  perc[j]=perc[i]
                  perc[i]=temp
    return perc

def bubble_sort(perc):
    for i in range(len(perc)-1):
        for j in range(0,len(perc)-i-1):
            if perc[j]>perc[j+1]:
                perc[j],perc[j+1]=perc[j+1],perc[j]
    return perc

def top_five(perc):
    if len(perc)<5:
          start,end=len(perc)-1,-1
    else:
        start,end=len(perc)-1,len(perc)-6
    
    for i in range(start,end,-1):
        return perc
    


a=input_percentage()
display_percentage(a)
selection_sort(a)
print("The Mark After Performing selection sort :\n",selection_sort(a))
print("The Mark After Performing bubble sort :\n",bubble_sort(a))
print("The top five element in the Array are :\n",top_five(a))
