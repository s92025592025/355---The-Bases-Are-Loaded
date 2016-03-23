import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int base1, base2;
			String number;
			base1 = sc.nextInt(); base2 = sc.nextInt();
			number = sc.next();
			if(!verify(base1, number.toUpperCase())){
				System.out.println(number + " is an illegal base " + base1 + " number");
			}else{
				System.out.println(number + " base " + base1 + " = " + convert(base1, number, base2) + " base " + base2);
			}
		}
	}

	public static boolean verify(int base, String number){
		for(int i = 0; i < number.length(); i++){
			if(number.charAt(i) > 64 && number.charAt(i) < 91){
				if(number.charAt(i) - 65 >= base){
					return false;
				}
			}else{
				if(number.charAt(i) - 48 >= base){
						return false;
				}
			}
		}

		return true;
	}

	public static String convert(int base1, String number, int base2){
		int sum = 0;
		int decimal = 1;
		for(int i = number.length() - 1; i > -1; i--){
			if(number.charAt(i) > 64 && number.charAt(i) < 91){
				sum += (number.charAt(i) - 65) * decimal;
			}else{
				sum += (number.charAt(i) - 48) * decimal;
			}

			decimal *= base1;
		}
		String converted = "";
		while(sum != 0){
			converted = sum % base2 + converted;
			sum = sum / base2;
		}

		return converted;
	}
}