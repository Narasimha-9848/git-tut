# Q1: Reverse a string
# Input: "hello"
# Output: "olleh"


# Q2: Check palindrome
# Input: "madam"
# Output: True  (it's a palindrome)

# Input: "python"
# Output: False (not a palindrome)

# Q3: Count vowels and consonants
# Input: "education"
# Output: Vowels = 5, Consonants = 5


# Q4: Character frequency
# Input: "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}


# Q5: Remove duplicates (keep first occurrence only)
# Input: "programming"
# Output: "progamin"

# Q6: First non-repeating character
# Input: "swiss"
# Output: "w"


# Q7: Longest common prefix
# Input: ["flower", "flow", "flight"]
# Output: "fl"

# Input: ["dog", "racecar", "car"]
# Output: ""  (no common prefix)


#Ans1
# s = 'hello'
# print(s[::-1])

#Ans2
# s = "madam1"

# s1 = s[::-1]

# if s == s1:
#     print("It's a Palendrome")
# else:
#     print("Not a Palendrome")

# Ans3
# vowels  = ['a','e','i','o','u']
# s = "education"
# vowels_count = []
# consonants_count = []
# for i in s:
#     if i in vowels:
#         vowels_count.append(i)
#     else:
#         consonants_count.append(i)
# print(f'vowels {len(vowels_count)}')
# print(f'consonants {len(consonants_count)}')

# Ans4
# s = "banana"
# s1={}
# for i in s:
#     if i not in s1:
#         s1[i] = 1
#     else:
#         s1[i]=s1[i]+1

# print(s1)


# Ans5
# s = 'programming'

# s1=[]
# for i in range(len(s)):
#     if s[i] not in s1:
#         s1.append(s[i])
    
# print("".join(s1))

# Ans6
# s = "Nissy"
# s1={}
# s2=[]
# for i in s:
#     if i not in s1:
#         s1[i] = 1
#     else:
#         s1[i]+=1
# for j in s1:
#     if s1[j] == 1:
#         s2.append(j)
# print(s2[0])

# Ans7
# Input: ["flower", "flow", "flight"]
# Output: "fl"

s =  ["flower", "flow", "flight"]
prefix = s[0]

for i in range(1,len(s)):
    while not s[i].startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            print("")
print(prefix)



    





        






