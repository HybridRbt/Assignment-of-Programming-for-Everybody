__author__ = 'jeredyang'

hrs = raw_input("Enter Hours:")
h = float(hrs)

rt = 10.50

if h > 40:
    gross_pay = (h - 40) * 1.5 * rt + 40 * rt
else:
	gross_pay = h * rt

print gross_pay