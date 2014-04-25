
# get user input on hours & rate
hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate per hour")

# calc pay & print
pay = float(hrs) * float(rate)
print pay # expect to be exactly the same with auto grader so no other prompt