__author__ = 'jeredyang'

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. The program looks for
 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python
  dictionary that maps the senders mail address to a count of the number of times they appear in the file.
  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most
  prolific committer.
"""

name = raw_input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

namecount = dict()

for line in handle:
    if line.startswith("From "):
        wl = line.split()
        namecount[wl[1]] = namecount.get(wl[1], 0) + 1

maxcount = None
maxname = None

for key, value in namecount.items():
    if maxcount is None or value > maxcount:
        maxcount = value
        maxname = key

print maxname + " " + str(maxcount)


