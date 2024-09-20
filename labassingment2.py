# Aim: In second year computer engineering class, group A student’s play cricket, group B students play badminton 
# and group C students play football. 
# Write a Python program using functions to compute following: -
# a) List of students who play both cricket and badminton 
# b) List of students who play either cricket or badminton but not both 
# c) Number of students who play neither cricket nor badminton 
# d) Number of students who play cricket and football but not badminton. 
# (Note- While realizing the group, duplicate entries should be avoided, Do not use SET builtin functions)


group_a = ["Shivam", "Ganesh", "Hari", "Rahul", "Aditya"]
group_b = ["Ganesh", "Aditya", "Aniket", "Jivan", "Samir"]
group_c = ["Rahul", "Ram", "Samarth", "Aditya"]

def duplicate_entry(*groups):
    duplicate_entry = set()
    for group in groups:
        duplicate_entry.update(group)
    return list(duplicate_entry)


def both_cric_badm(group_a, group_b):
    both = []
    for i in group_a:
        if i in group_b and i not in both:
            both.append(i)
    return both

def either_cric_or_badm(group_a, group_b):
    either = []
    for i in duplicate_entry(group_a + group_b):
        if (i in group_a) != (i in group_b):
            either.append(i)
    return either

def count_neither(group_a, group_b, total_students):
    neither_count = 0
    for i in total_students:
        if i not in group_a and i not in group_b:
            neither_count += 1
    return neither_count

def cric_footb_not_badm(group_a, group_c, group_b):
    count = 0
    for i in group_a:
        if i in group_c and i not in group_b:
            count += 1
    return count

total_students = duplicate_entry(group_a, group_b, group_c)
print("Students who play both cricket and badminton:",both_cric_badm(group_a, group_b))
print("Students who play either cricket or badminton but not both:", either_cric_or_badm(group_a, group_b))
print("Number of students who play neither cricket nor badminton:", count_neither(group_a, group_b, total_students))
print("Number of students who play cricket and football but not badminton:", cric_footb_not_badm(group_a, group_c, group_b))
