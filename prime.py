#This 'prime.py' module simply lists all the prime numbers.
#First it prompts the user to enter a number. 
# Then the entered number which is actually a string is 
#converted to the integer.Then the prime(num) function is called 
#which finds all the prime numbers upto the entered number on the screen

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


