######################################################################################################################

# Kata 6 kyu Vasya - Clerk
# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a 
# huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
# Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly 
# in the order people queue?
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
# Otherwise return NO.
# Examples:
# tickets([25, 25, 50]) # => YES 
# tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars

def tickets(people):
    tick25 = 0
    tick50 = 0
    tick100 = 0
    for tick in people:
        if tick == 25:
            tick25 += 1
        elif tick == 50:
            tick50 += 1
            if tick25 == 0:
                return "NO"
            tick25 -= 1
        elif tick == 100:
            tick100 += 1
            if tick50 > 0 and tick25 > 0:
                tick50-=1
                tick25-=1
            elif tick25 >= 3:
                tick25 = tick25-3
            else:
                return "NO"
    return "YES"

######################################################################################################################

# Highest and Lowest
# In this little assignment you are given a string of space separated numbers, and have to return the highest
# and lowest number.
# Example:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    new_numbers = list(map(int, (numbers.split(' '))))
    min_num = str(min(new_numbers))
    max_num = str(max(new_numbers))
    result = ''.join(max_num + ' ' + min_num)
    return result


######################################################################################################################

#Kata 6 kyu. Counting Duplicates
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric 
#digits that occur more than once in the input string. The input string can be assumed to contain only alphabets
#(both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'

def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for item in text:
        if text.count(item) > 1 and item not in duplicates:
            duplicates.append(item)    
    return len(duplicates)

######################################################################################################################

#Kata 6 kyu. Sum of Digits / Digital Root
# In this kata, you must create a digital root function.
# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. 
#If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
#This is only applicable to the natural numbers.
# Here's how it works:
# digital_root(16)
# => 1 + 6
# => 7

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

######################################################################################################################

# Kata 6 kyu: Reverse every other word in the string
# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, 
# while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are apart
# of the word in this kata.

def reverse_alternate(string):
  if string == "":
      return ""
  else:
      newArr = []
      for i in range(len(string.split())):
          if i%2 != 0:
              newArr.append(string.split()[i][::-1])
          else:
              newArr.append(string.split()[i])
      return " ".join(newArr)

######################################################################################################################

# Hex Word Sum
# Description
# As hex values can include letters A through to F, certain English words can be spelled out, such as CAFE, BEEF, or FACADE. 
# This vocabulary can be extended by using numbers to represent other letters, such as 5EAF00D, or DEC0DE5.
# Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.
# Example
# Working with the string BAG OF BEES:
# BAG ==> 0 as it is not a valid hex value

def hex_word_sum(s):
  return sum(int(x, 16) for x in s.replace('O', '0').replace('S', '5').split() if all(y in '0123456789ABCDEF' for y in x))

######################################################################################################################

# Count the number of occurrences of each character and return it as a list of tuples in order of appearance.
# Example:

def ordered_count(input):
    return [(x, input.count(x)) for x in sorted(set(input), key=input.index)]

######################################################################################################################

#Kata 6 kyu: Return 1, 2, 3 randomly
# You have function one_two (oneTwo for Java) that returns 1 or 2 with 50% chance. one_two is already defined in a global 
#scope and can be called everywhere.
# Your goal is to create function one_two_three (oneTwoThree for Java) that returns 1, 2 or 3 with equal probability 
#using only one_two function.
# Do not try to cheat returning repeating non-random sequences. There is randomness test especially for this case.

def one_two_three():
    r = one_two() * 3 + one_two()
    return 1 if r == 4 else 2 if r == 5 else 3 if r == 7 else one_two_three()

######################################################################################################################

# If　a = 1, b = 2, c = 3 ... z = 26
# Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# So friendship is twice stronger than love :-)
# The input will always be in lowercase and never be empty.
#test.assert_equals(words_to_marks('attitude'), 100)

def words_to_marks(s):
    base = ord('a') - 1
    return sum(ord(l) - base for l in s)

######################################################################################################################

#Kata 6 kyu: Who likes it?
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who
#  like an item. It must return the display text as shown in the examples:
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)

######################################################################################################################

# Introduction and Warm-up (Highly recommended)
# Playing With Lists/Arrays Series
# Task
# Given an array/list [] of integers , Find the product of the k maximal numbers.
# Notes
# Array/list size is at least 3 .
# Array/list's numbers Will be mixture of positives , negatives and zeros
# Repetition of numbers in the array/list could occur.
# Input >> Output Examples
# maxProduct ({4, 3, 5}, 2) ==>  return (20)

def max_product(lst, n_largest_elements):
    dCtver1 = sorted(lst,reverse=True)
    dCtver2 = dCtver1[0:n_largest_elements]
    n_largest_elements = 1
    for i in dCtver2:
        n_largest_elements *= i
    return n_largest_elements


######################################################################################################################

# Task
# Given a number , Return _The Maximum number _ could be formed from the digits of the number given .
# Notes
# Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive !alt !alt
# Digit Duplications could occur , So also consider it when forming the Largest !alt
# Input >> Output Examples:
# maxNumber (213) ==> return (321)

def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))

# solution in details
def max_number(n):
    new = str(n)    #меняем тип
    new = list(map(int, new)) #преобразовываем строку в список чисел
    new = sorted(new, reverse=True) #сортируем по убывани (впринципе задача решена)
    new2 = ''.join(str(i) for i in new) #в джоине идем по списку и каждую итерацию преобразовываем в str по списку 
    #и записываем все в строку
    new2 = int(new2)    #преобразовываем в int
    return new2

######################################################################################################################

# Find the first non-consecutive number
# 1454490% of 1,3683,461 of 9,718thecodeite
# Python
# TRAIN AGAINNEXT KATA
# Details
# Solutions
# Forks (11)
# Discourse (51)
# Collect|
# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's
# the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be 
#unique and in ascending order. 
#The numbers could be positive or negative and the first non-consecutive could be either too!

def first_non_consecutive(a):
    i = a[0] 
    for e in a:
        if e != i:
            return e
        i += 1
    return None

######################################################################################################################

# Description:
# Remove all exclamation marks from sentence except at the end.
# Examples
# remove("Hi!") == "Hi!"
# remove("Hi!!!") == "Hi!!!"
# remove("!Hi") == "Hi"
# remove("!Hi!") == "Hi!"
# remove("Hi! Hi!") == "Hi Hi!"
# remove("Hi") == "Hi"

def remove(s):
    stripped = s.rstrip("!")
    newS = s.replace("!", "")
    outLen = len(s) - len(stripped)
    count = "!"*outLen
    newS += count
    return newS

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