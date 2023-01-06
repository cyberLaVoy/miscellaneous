
def euclid(a, b):
	if b == 0:
		return (1, 0, a)
	(x, y, d) = euclid(b, a % b)
	return (y, x - (a//b)*y, d)

def main():
	print(euclid(12, 5))
main()
