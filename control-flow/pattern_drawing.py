size = int(input("Enter the size of the pattern: "))
size2 = size

while size > 0:
	print("*", end="")
	for num in range(1, size2):
		print("*", end="")
	print("")
	size-= 1