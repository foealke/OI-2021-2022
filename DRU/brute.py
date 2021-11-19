data = ""
for m in range(1, 1000):
	for n in range(1, 1000):
		counter = 0
		for i in range(1, max(n,m)):
			if (m*n) % i == 0:
				counter+=1
		data += str(m)+";"+str(n)+";"+str(counter)+"\n"
	print("Progress: ", ((m/1000)*100), " %")	

with open("data.csv","a") as file:
	file.write(data)
