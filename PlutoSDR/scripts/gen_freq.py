max = 3800
min = 325
step = 20
freq = []
while (min < max):
	freq.append(str(min) + "000000")
	min = min + step
print("freq = " + str(freq).replace('\'', ''))
print(len(freq))