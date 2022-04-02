#Practice using the Python interpreter as a calculator:

#The volume of a sphere with radius r is (4/3)πr^3. What is the volume of a sphere with radius 5?

pi = 3.14159
r = 5
v = (4/3)*pi*r**3
v		# 523.5983333333332
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

x = 60
unit_cost = 24.95 * 0.6
total_shipping = 3 + (0.75 * x)
total_cost = (unit_cost * x) + total_shipping
total_cost		# 946.1999999999999
#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

# calculate time spent running in seconds
# run starts and ends with 1 mile @ 8:15/mile
# total 2 miles @ 8:15/mile
time_1_seconds = ((8 * 60) + 15) * 2
# middle of run is 3 miles @ 7:12 per mile
time_2_seconds = ((7 * 60) + 12) * 3
total_seconds = time_1_seconds + time_2_seconds
# convert time spent running to minutes, seconds
minutes = total_seconds // 60
seconds = total_seconds % 60
print(str(minutes) + ', ' + str(seconds))

# calculate return time
hour = 7
# 8 minutes remaining in previous hour
minute = minutes - (60 - 52)

# print return time
print(str(hour) + ":" + str(minute))
