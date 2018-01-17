# coding: utf-8


"""
Here’s another Car Talk Puzzler you can solve with a search ( http: // www.
cartalk. com/ content/ puzzlers ):

“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.

“When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and
if we’re really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”

Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
method zfill useful.

Solution: http: // thinkpython. com/ code/ cartalk3. py .
"""

"""
Description
The method zfill() pads string on the left with zeros to fill width.

Syntax
Following is the syntax for zfill() method −
str.zfill(width)

Parameters
width − This is final width of the string. This is the width which we would get after filling zeros.

Return Value
This method returns padded string.
"""


def count():
    son = 0
    mom = 36

    i = 0
    while i < 9:
        str_mom = str(mom)
        str_son = str(son).zfill(len(str_mom))
        if str_mom == str_son[::-1]:
            i += 1
            print i
            print 'mom :', mom
            print 'son :', son
            print ''

        mom += 1
        print mom
        son += 1


count()
