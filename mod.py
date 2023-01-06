

def modexp(x,y,n):
	if y == 0:
		return 1
	z = modexp(x, y//2, n)
	if y % 2 == 0:
		return z**2 % n
	else:
		return x*z**2 % n

def main():
	p = 10
	z = modexp(6, 21, p)
	print(z)
	a = modexp(7, z, p)
	print(a)
	
main()
