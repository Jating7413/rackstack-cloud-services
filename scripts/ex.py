f = open("C:/users/Jatin Gupta/Desktop/yay.txt" , 'r')
entry = f.read()
f.close()
b = []
b.append(entry.split(":"))

print(b)

entry1 = "a3"

if b[0][0] == "jojo":
	print("hah")

for sublist in b:
	if entry1 in  sublist:
		print("hey")