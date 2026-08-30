#patterns

# Right Triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")

#Note : we can consider  from i=1,i=5 cause need to print starts based on i

#Left Triangle

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print("")

#Right sided
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

#Left sided

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()


#Hill station or pyramid

n = 5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()

#Reverse Hill or Reverse Pyramid

n = 5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for l in range(i,n-1):
        print("*",end=" ")
    print()

# Double hill
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     for l in range(i,n-2):
#         if i == 3 or i ==4:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         print("",end=" ")
#     limit = i+1 if i!=n-1 else i
#     for m in range(limit):
#         print("*",end=" ")
#     print()
