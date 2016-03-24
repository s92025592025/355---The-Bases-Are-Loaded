def main():
	while True:
		base1, base2, number = raw_input().split()
		base1 = int(base1)
		base2 = int(base2)
		if not verify(base1, number):
			print(number, " is an illegal base ", base1, " number")
		else:
			print(number, " base ", base1, " = ", transfer(base1, number, base2), " base ", base2)

def convert(c):
	if c[0] > 64 and c[0] < 91:
		return ord(c[0]) - 55

	return ord(c[0]) - 48

def verify(base, number):
	if len(number) == 1:
		return convert(number[0]) < base

	if convert(number[0]) >= base:
		return False

	return verify(base, number[1 : ])

def transfer(base1, number, base2):
	totalSum = total(base1, number)
	converted = "";
	if(totalSum == 0):
		return "0"

	while total != 0:
		converted = convertBack(totalSum % base2) + converted
		totalSum = totalSum / base2

	return converted

def total(base, number):
	totalSum = 0
	decimal = 1
	for i in reversed(range(0, len(number))):
		totalSum += convert(number[i]) * decimal;
		decimal *= base;

	return totalSum

def convertBack(digit):
	if digit > 9:
		return char(digit + 55)

	return str(digit)

if __name__ == "__main__":
	main()