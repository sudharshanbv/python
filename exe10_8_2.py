
# coding: utf-8

"""
If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module.
You can read about this problem at http: // en. wikipedia. org/ wiki/ Birthday_ paradox ,
and you can download my solution from http: // thinkpython. com/ code/ birthday. py .
"""

import random

for i in range(22):
    print random.randint(1, 30)
