import os
data = []

input_file = open("1.in", "r")
number_lines = input_file.readlines()
rdfile = input_file.read()
rawfile = open("1.rin", "r")
rawread = rawfile.read()
count = 0
elves = 0
top3list = []
calories = 0
most = 0
for line in number_lines:
	if line.strip() == "":
		elves += 1
	else:
		count += 1
		print("{}: {}".format(count, line.strip()))

for l in rawread.split('\\n'):
	if len(l) == 0:
		top3list.append(calories)
		calories = 0 
		continue
	calories += int(l)

print(f"{elves} elves.")
print(f"{count} calorie lines.")
print(f"{most} most calories")
print(top3list[-3:])
top3list.sort()
print(top3list[-3] + top3list[-2] + top3list[-1])

	