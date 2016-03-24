#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int alphabetToNum(char c);
bool verify(int base, string number);
string convert(int base1, string number, int base2);
long toBaseTen(int base, string number);
string numToAplhabet(long digit);

int main(){
	int base1, base2;
	string number;
	while(cin >> base1 >> base2 >> number){
		if(!verify(base1, number)){
			cout << number << " is an illegal base " << base1 << " number" << endl;
		}else{
			cout << number << " base " << base1 << " = " << convert(base1, number, base2) << " base " << base2 << endl;
		}
	}
	return 0;
}

int alphabetToNum(char c){
	if(c > 64 && c < 91){
		return c - 55;
	}

	return c  - 48;
}

bool verify(int base, string number){
	if(number.length() == 1){
		return alphabetToNum(number[0]) < base;
	}

	if(alphabetToNum(number[0]) >= base){
		return false;
	}

	return verify(base, number.substr(1, number.length() - 1));
}

string convert(int base1, string number, int base2){
	long sum = toBaseTen(base1, number);
	string converted = "";
	do{
		converted = (numToAplhabet(sum % base2)) + converted;
		sum = sum / base2;
	}while(sum != 0);

	return converted;
}

long toBaseTen(int base, string number){
	long sum = 0;
	long decimal = 1;
	for(int i = number.length() - 1; i > -1; i--){
		sum += alphabetToNum(number[i]) * decimal;
		decimal *= base;
	}

	return sum;
}

string numToAplhabet(long digit){
	if(digit < 10){
		return to_string(digit);
	}
	stringstream ss;
	string s;
	ss << (char)(55 + digit);
	ss >> s;
	return s;
}