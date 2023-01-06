import subprocess

def webpages():
	fin = open("websites.txt", "r")
	for line in fin:
		line = line.strip()
		subprocess.call(["open", line])
	fin.close()

def run():
	value = input("ready to rumble?(y/n): ")
	while value != "y" and value != "n":
		value = input("ready to rumble?(y/n): ")
	return value

def main():
	value = run()
	if value == "y":
		webpages()
	else:
		print("okay")
main()

