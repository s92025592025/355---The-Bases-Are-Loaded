# 355---The-Bases-Are-Loaded

<h5>Java:</h5>
<p>Really not much new concepts to talk about, only need to notice that it needs a long to store the base 10 value, int may overflow when it reached base over 16</p>

<h5>C++:</h5>
<p>When trying to return a string in a method, make sure to include <string>, or it will definitely fail to compile. Converting char to string is not as easy as Java, and we have to use stringstream. Include <sstream>, then initinalize a stringstream variable. Pass the char in the variable with << and then pass it out to a string variable using >>. </p>

<p>Example code:</br>
stringstream ss;</br>
ss << char;</br>
ss >> string;</br></p>

<h5>Python:</h5>
<p>A lot of new things to talk about. Firstly, raw_input()(2.7) and input()(3.X) reads the whole line and return a string, and there seems to be no built in function that works like .next() or .nextInt() from Java in Python. One way of reading the input by spaces is to store the string, then use the spilt() function to get a list of input.</p>

<p>Example code:</br>
inputList = raw_input().split()</br>
variable1 = inputList[0]</br>
variable2 = inputList[1]</br>
.</br>
.</br>
.</br>
etc</p>

<p>Another thing to talk about is the convertion between string, char and int. I'm going to break down to <b>"everything to string"</b>, <b>"char to int and int to char"</b> and <b>"string to int"</b></p>

<ul>
  <li>everything to string</br>
  <p>In this bullet point I'm talking about casting the excat same content of the variable to string. The function we need is only str(), it accepts one parameter which is the stuff we want to cast to a string. It will return a string that contains the original context but in string format</p></li>
  <li>char to int and int to char</br>
  <p>What wee want to do hewre is to convert the char to it's correspoding ASCII value, and the finction to use is ord(). It accpets one char parameter, and returns a int corresponding to its ASCII value. To do thid job backwords, we can use function chr(). It accepts one int parameter and returns a char that corresponds to the int ASCII value</p></li>
  <li>string to int</br>
  <p>In Java we have Integer.ParseInt(String s) for this. In Python, we've got int(). It can accept a string that its context are puyly number without spaces in the middle, and convert the data type to int.</p></li>
</ul>

<p>One last thing about Python in this problem. Python is the only on e that I don't have to worry about the integer overflow. Even if I started the variable like an int, it will automatically charnge to long by itself when it needs to</p>
