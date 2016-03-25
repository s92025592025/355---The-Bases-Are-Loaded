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

<p>Another thing to talk about is the convertion between string, char and int. I'm going to break down to <b>"everything to string"</b>, <b>"char to int"</b>, <b>"int to char"</b> and <b>"string to int"</b></p>
