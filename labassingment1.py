# Write a Python program to store marks scored in subject "Fundamental of Data Structure" by N students in the class.
#  Write functions to compute following:

# a) The average score of class

# b) Highest score and lowest score of class

# c) Count of students who were absent for the test

# d) Display mark with highest frequency

# def average(marks):
#     total=0;
#     count=0;
#     for  i in range(len(marks)):
#         if marks[i]!=-999;


n=int(input("Enter Number Of Students :"))

def input_marks():
    marks=[]
    for i in range(n):
        marks.append(float(input("Enter Marks Of Students {0} :".format(i+1))))
    return marks

def display_marks(marks):
    for i in range(len(marks)):
            print("Marks of Student {0}:".format(i + 1),marks[i])


def average_marks(marks):
    total=0;
    for  i in range(len(marks)):
        if marks[i]>0:
            total+=marks[i]
        avg=total/n
    print("Average Marks Is :",avg)

def max_marks(marks):
    maxvalue=marks[0]
    minvalue=marks[0]
    for i in range(len(marks)):
        if marks[i]>maxvalue:
            maxvalue=marks[i]
        elif marks[i]<minvalue:
            minvalue=marks[i]
    print("Highest Score In The Students :",maxvalue)
    print("Lowest Score In The Students :",minvalue)

def absent_student(marks):
    abs= n-len(marks)
    print("The Absent Student In The Exam Are:",abs)

def highest_frequency_marks(marks):
    for i in range(0,len(marks)):
        for j in range(i+1,len(marks)):
            if marks[i]==marks[j]:
                print("The Highest Frequency Of The Marks Is :",marks[i])
                break;

    
a=input_marks()
display_marks(a)
average_marks(a)
max_marks(a)
absent_student(a)
highest_frequency_marks(a)