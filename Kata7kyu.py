#In this Kata, you will be given a lower case string and your task will be to remove k characters from 
#that string using the following rule:
#For example: 
#solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
#solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
#solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 

def solve(st,k): 
    for letter in sorted(st)[:k]:
        st = st.replace(letter,'',1)
    return st

######################################################################################################################
# Task
# Given a string s, find out if its characters can be rearranged to form a palindrome.
# Example
# For s = "aabb", the output should be true.
# We can rearrange "aabb" to make "abba", which is a palindrome.
# Input/Output
# [input] string s
# A string consisting of lowercase English letters.

def palindrome_rearranging(s):
    count = 0
    for i in set(s):
        if s.count(i) % 2 != 0:
            count += 1
    if count > 1:
        return False
    else:
        return True

######################################################################################################################

# ⚠️ The world is in quarantine! There is a new pandemia that struggles mankind. 
# Each continent is isolated from each other but infected people have spread before the warning. ⚠️
# 🗺️ You would be given a map of the world in a type of string:
# string s = "01000000X000X011X0X"
# '0' : uninfected
# '1' : infected
# 'X' : ocean⚠️ 


def infected(s):
    lands = s.split('X')
    total = sum(map(len, lands))
    infected = sum(len(x) for x in lands if '1' in x)
    return infected * 100 / (total or 1)

######################################################################################################################

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    m = []
    for (i, j) in enumerate(lines):
        m.append("" + str(i+1) + ": " + str(j))
    return m

######################################################################################################################

# The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the
# two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].
# The order of the numbers passed in could be any order. The array will always include at least 2 items.

def two_oldest_ages(ages):

    n = max(ages)
    ages.remove(n)
    m = max(ages)
    a = []
    a.append(n)
    a.append(m)
    a.sort()
    return a

######################################################################################################################

# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# Output:
# 'alpha beta gamma delta'

def remove_duplicate_words(s):
    y = s.split()
    z = list()
    for i in y:
        if i not in z:
            z.append(i)
    return " ".join(z)

######################################################################################################################
