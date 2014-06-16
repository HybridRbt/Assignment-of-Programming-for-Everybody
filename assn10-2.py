__author__ = 'jeredyang'

"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that
the autograder does not have support for the sorted() function.
"""

name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

hrcount = dict()

for line in handle:
    if line.startswith("From "):
        for c_index in range(0, len(line)):
            # first cha is a digit
            if line[c_index].isdigit():
                # second cha is a digit
                if line[c_index + 1].isdigit():
                    # third cha is ":"
                    if line[c_index + 2] == ":":
                        # found time segment, get line[c_index : c_index + 1]
                        hr = line[c_index: c_index + 2]
                        if hr in hrcount:
                            hrcount[hr] += 1
                        else:
                            hrcount[hr] = 1
                        break

hr_lst = []

for key, value in hrcount.items():
    hr_lst.append((key, value))

hr_lst.sort()
print hr_lst