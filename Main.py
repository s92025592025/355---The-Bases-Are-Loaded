def main():
	while True:
		inputString = raw_input().split()
		if(len(inputString) < 3):
			break
		base1 = int(inputString[0])
		base2 = int(inputString[1])
		number = inputString[2]
		if not verify(base1, number):
			print number + " is an illegal base " + str(base1) + " number"
		else:
			print number + " base " + str(base1) + " = "  + transfer(base1, number, base2) + " base " + str(base2)

def convert(c):
	if ord(c[0]) > 64 and ord(c[0]) < 91:
		return ord(c) - 55

	return ord(c) - 48

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
	while totalSum != 0:
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
		return str(chr(digit + 55))

	return str(digit)

if __name__ == "__main__":
	main()
