# Reverse String
# s = "hello"
# print(s[::-1])

#frequency counter
# s = "programming"
# count=0
# for i in s:
#     if i == 'g':
#         count=count+1
# print(count)

# Palendrome
# s = "madam"
# check_pal = s[::-1]
# if s == check_pal:
#     print("palindrome")
# else:
#     print("Not a palindrome")

#Anagram

# s = "listen"
# s1 = "silent"
# if len(s) == len(s1):
#     a1="".join(sorted(s))
#     b1="".join(sorted(s1))
#     if a1 == b1:
#         print("Anagram")
#     else:
#         print("Not Anagra")
# else:
#     print("Not Anagram")


# 1.Traversing a string
# s = "hello"
# for i in s:
#     print(i,end=" ")

# 2. Character counting
# s = "mississippi"
# print(len(s))

# 3.Character frequency
# s = 'banana'
# s2={}
# for i in s:
#     if i not in s2:
#         s2[i]=1
#     else:
#         s2[i]+=1
# print(s2)



# 6.vowels/consonants

# s = "education"
# sample = ['a','e','i','o','u']

# v_c=0
# c_c=0

# for i in s:
#     if i in sample:
#         v_c=v_c+1
#     else:
#         c_c=c_c+1
# print(v_c)
# print(c_c)


# 7. Remove character

# s = "hello world"

# if 'l' in s:
#     s2= s.replace('l','')
# print(s2)

# 8. Duplicate character
# s = "programming"
# s2={}
# s3={}
# for i in s:
#     if i not in s2:
#         s2[i]=1
#     else:
#         s3[i]=s2[i]+1
# print(s3)

# 9. Find maxi/min char

# s = "zebra"
# s3=[]
# for i in s:
#     s3.append(ord(i))
# s4 = sorted(s3)
# min_vlaue = chr(s4[0])
# max_value = chr(s4[-1])
# print(min_vlaue)
# print(max_value)


# 11. substrings
# s = "abcd"
# for i in range(len(s)+1):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])

# s = "abcd"
# count=0
# for i in range(len(s)+1):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])
#         count+=1
# print(count)


# s = "banana"
# count=0
# for i in range(len(s)+1):
#     for j in range(i+1,len(s)+1):
#         out = s[i:j]
#         if out == 'ana':
#             count+=1
# print(count)
    
#problems by chatgpt
# first non-repeating character

# s = "aabbcddee"
# s2={}
# for i in range(len(s)):
#     if s[i] not in s2:
#         s2[s[i]]=1
#     else:
#         s2[s[i]]+=1

# for ch in s:
#     if s2[ch] == 1:
#         print(ch)
#         break



# remove duplicate character

# s = "programming"
# s1=[]
# for i in range(len(s)):
#     if s[i] not in s1:
#         s1.append(s[i])
# print("".join(s1))

# Character with highest frequency

# s = "mississippi"
# s2={}
# for i in range(len(s)):
#     if s[i] not in s2:
#         s2[s[i]]=1
#     else:
#         s2[s[i]]+=1
# highest = max(s2.values())
# for key,value in s2.items():
#     if s2[key] >= highest:
#         highest = s2[key]
#         out = key
#         break;

# print(out)

    
# count substring
# s = "abababababab"
# sub = "ab"
# out = ""
# count=0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         calc_sub = s[i:j]

#         if sub == calc_sub:
#             count+=1

# print(count)

# first duplicate characte
# s = "abcdaf"

# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i] == s[j]:
#             print(s[i])
#             break;
#     break;

# find max element in the array
# arr = [10, 5, 20, 8, 15]
# high = arr[0]
# for i in arr:
#     if i>=high:
#         high = i
# print(high)

# find the minimum element in the list
# arr = [10, 5, 20, 8, 15]
# low = arr[0]
# for i in arr:
#     if i<=low:
#         low = i
# print(low)

# find sum of all elements in list
# arr = [10, 5, 20, 8, 15]
# total=0
# for i in arr:
#     total+=i
# print(total)

# Count how many even and odd numbers are present.

# arr = [10, 5, 20, 8, 15, 7, 12]
# count_even = 0
# count_odd = 0
# for i in arr:
#     if i%2 == 0:
#         count_even+=1
#     else:
#         count_odd+=1
# print(count_even)
# print(count_odd)

# arr = [-10, 5, -20, 8, 15, -7, 12, 0]
# count_zero=0
# count_pos=0
# count_neg=0
# for i in arr:
#     if i==0:
#         count_zero+=1
#     elif i>0:
#         count_pos+=1
#     else:
#         count_neg+=1
# print(count_zero)
# print(count_pos)
# print(count_neg)

#Search an Element
# arr = [10, 5, 20, 8, 151, 7, 12]
# target = 15
# found = False
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found")
#         print(f"Index {i}")
#         found = True
#         break;
# if not found:
#     print("Not Found")

# Reverse an array

# arr = [1, 2, 3, 4, 5]
# reversed_arr = []
# for i in range(len(arr)-1,-1,-1):
#     reversed_arr.append(arr[i])
# print(reversed_arr)
    
# find second largest element
# arr = [10, 5, 20, 8, 15,3,4]
# arr = [10,20,5,15,2,4,6]
# first=arr[0]
# second=arr[-1]
# for i in range(len(arr)):
#     if arr[i]>=first:
#         first=arr[i]
# for i in range(len(arr)):
#     if arr[i]<first and arr[i]>second:
#         second=arr[i]

# print(second)

# for i in range(len(arr)):
#     if arr[i]>=first:
#         second = first
#         first = arr[i]
#     elif arr[i]<first and arr[i] > second:
#         second = arr[i]
# print(second)

# for i in range(len(arr)):
#     if arr[i]>=first:
#         second = first
#         first = arr[i]
#     elif arr[i]>second:
#         second=arr[i]
# print(second)

# arr = [10, 20, 20, 15,19]
# first = arr[0]
# for i in range(len(arr)):
#     if arr[i]>= first:
#         first = arr[i]
#     elif arr[i]<first:
#         second = arr[i]
# print(second)


# arr = [50, 12, 80, 35, 70, 25]
# first=arr[0]
# for i in range(len(arr)):
#     if arr[i]>=first:
#         first = arr[i]
# second = arr[0]
# for i in range(len(arr)):
#     if arr[i]<first and arr[i]>second:
#         second = arr[i]
# print(second)


# arr = [5, 2, 8, 1, 6]

# first = arr[0]
# for i in range(len(arr)):
#     if arr[i]>first:
#         first = arr[i]
# second=arr[0]
# for i in range(len(arr)):
#     if arr[i]<first and arr[i]>second:
#         second = arr[i]
# print(second)

# arr = [-10, -5, -20, -8, -15]

# first = arr[0]

# # for i in range(len(arr)):
# #     if arr[i]>=first:
# #         first = arr[i]
# # print(first)
# # second=float('-inf')
# # for i in range(len(arr)):
# #     if arr[i]<first and arr[i]>second:
# #         second=arr[i]

# # print(second)

#########################################
#List Problems
#########################################

# arr = [1, 2, 3, 2, 4, 1, 5, 3]
# duplicates = []
# non_duplicates = []
# for i in range(len(arr)):
#     if arr[i] not in non_duplicates:
#         non_duplicates.append(arr[i])
#     else:
#         duplicates.append(arr[i])
# print(duplicates)

# arr = [1, 2, 2, 2, 3]

# duplicates = []
# non_duplicates = []

# for i in range(len(arr)):
#     if arr[i] not in non_duplicates:
#         non_duplicates.append(arr[i])
#     else:
#         if arr[i] not in duplicates:
#             duplicates.append(arr[i])

# print(duplicates)

# arr = [10, 20, 10, 30, 20, 40, 10]
# check_frq = {}
# for i in range(len(arr)):
#     if arr[i] not in check_frq:
#         check_frq[arr[i]] = 1
#     else:
#         check_frq[arr[i]]+=1

# print(check_frq)

# arr = [10, 20, 10, 30, 20, 40, 10]
# check_freq={}
# for i in range(len(arr)):
#     if arr[i] not in check_freq:
#         check_freq[arr[i]]=1
#     else:
#         check_freq[arr[i]]+=1
# highest_frequency = float('-inf')
# highest_element = None
# for key,value in (check_freq.items()):
#     if value >= highest_frequency:
#         highest_frequency =value
#         highest_element = key

# print(highest_element)


arr = [10, 5, 20, 8, 15]
target = 20
total = 0
for i in range(len(arr)):
    if arr[i] == target:
        break;
    total+=arr[i]
print(total)

arr = [4, 7, 2, 9, 5, 3]
target = 9
total=0
for i in range(len(arr)):
    total+=arr[i]
    if arr[i] == target:
        break;
print(total)



