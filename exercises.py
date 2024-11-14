"""
Question 1
Given this string of comma separated characters, create three new variables
containing the unicode codepoint (in hex), uppercase and lower case versions
of each character (also comma delimited).

For example, if the string was 'a, b, c' you should generate three lists that
look like:

['0x61', '0x62', '0x63']
['a', 'b', 'c']
['A', 'B', 'C']
[You should use the split() and strip() functions, amongst others, to help you
solve this.]
s = 'Π, ύ, θ, ω, ν'
"""
s = 'Π, ύ, θ, ω, ν'
characters = s.split(', ')
codepoint = [hex(ord(char)) for char in characters]
lower_chars = [char.lower() for char in characters]
upper_chars = [char.upper() for char in characters]
print(characters)
print(codepoint)
print(lower_chars)
print(upper_chars)
print()



"""
Question 2
Using two types of string interpolation, and given the variable a that 
contains an integer, print out the following string for a:

The number ...value of a... is (or is not) even

For example, if a is 42, the your code should print:

'The number 42 is even'

But if a is 31, then the same code should print:

'The number 31 is not even'
"""



"""
Question 3
You are given two variables a and b (with b non-zero), and you need to 
generate a string that reads something like this:

'a / b = (result)'
But you want your string to be nicely formatted for display purposes, so you 
want to limit displaying possible digits after the decimal point in all your 
values to 4 digits.
"""




