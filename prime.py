def prime(num):
	p = 2
	while p**2 <= input:
		for i in num:
			if int(i) > p and int(i) % p ==0:
				num.remove(i)
		p += 1
		print(p)

input = int(raw_input('Enter a number: '))
num = range(2,input + 1)
print(num)		
prime(num)

print(num)


