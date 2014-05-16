__author__ = 'jeredyang'

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"


# def revert_string(string):
#     result = ""
#     for index in range(len(string) - 1, -1, -1):
#         result += string[index]
#
#     return result
#
#
# rev_text = revert_string(text)
# sliced_text = rev_text[:rev_text.find(" ")]
#
# print float(revert_string(sliced_text))

sliced_text = text[text.find(" "):]
print float(sliced_text)

