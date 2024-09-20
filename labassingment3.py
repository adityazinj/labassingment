import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(A,"\n""\n",B)

# Addition Of The Matrices
print("\n")
addition_matri=A+B

print("The Addition Of The Matrix A And B Is :\n", addition_matri)
# print("\n")

# Substraction Of the Matrices

print("\n")
substaction_matri=A-B

print("The Substraction Of The Matrix A And B Is :\n", substaction_matri)
# print("\n")


# Multiplication Of the Matrices

print("\n")
multiplication_matri=A*B

print("The Multiplication Of The Matrix A And B Is :\n", multiplication_matri)
# print("\n")



print("\n")
# if B!=0:
if np.all(B!=0):
    division_matri=A/B
    print("The Division Of The Matrix A And B Is :\n\n",division_matri)
    print("\n")
else:
    print("Invalid Value Of B")

# Transpose The Matrix 
print("The Transpose Of The MAtrix A Is :\n")

transpose_matri_A=A.T
print(transpose_matri_A)
print("\n")

print("The Transpose Of The MAtrix B Is :\n")

transpose_matri_B=B.T
print(transpose_matri_B)



