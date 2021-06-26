import password
fname = input("file name: ")
# mode = input("Enter mode: ")
# f = open(fname,"x")
with open(fname,"a+") as f:
	f.seek(0)
	data = f.read(100)
	if len(data)>0:
		f.write("\n")	
	f.write(f"{password.purpose} password : {password.password}")
print("Entered successfully.................")
f.close()



