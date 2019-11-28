Please deliver this homework as .py file.

## Question 1
Below you'll see a list of numbers, print the list of even numbers and the list of uneven numbers. For this you'll need the ```%``` (modulo) operator, use the internet to find out how that works!

```python
numbers = [8984, 288, 7842, 5926, 3243, 6630, 4, 4868, 7482, 9139, 6060, 1959, 5899, 2944, 761, 9661, 1471, 8072, 2674, 8116, 1724, 1855, 9362, 7842, 3080, 1906, 1010, 6111, 3320, 7378, 1090, 3283, 6528, 1445, 7466, 16, 3544, 7569, 6445, 9599, 7836, 511, 7253, 1971, 611, 9410, 6962, 4899, 7518, 3343, 7381, 5157, 4412, 646, 1183, 8385, 3011, 3960, 8403, 124, 2155, 3101, 1972, 2301, 1624, 297, 28, 9875, 7608, 1854, 252, 2513, 154, 5058, 4402, 5653, 1069, 1400, 6614, 5800, 7170, 8677, 7106, 9412, 3096, 1423, 1130, 1002, 5903, 1520, 7017, 7990, 7847, 4427, 497, 6797, 4023, 1996, 2979, 5145]
```

## Question 2

Using the same list of numbers, print the total sum of all the number. Also print the sum of all the even numbers and the sum of all the odd numbers. Are there more odd or even numbers in this list?

## Question 3

Write a program that generates the following pattern
```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
```
### hints:
- You probably need multiple for-loops for this. 
- First construct a list of lists containing every line, like this:
```python
>>> ['*', '* *', '* * *', etc ..
```
- By default, every print() print on a new line. If you want to you can prevent this by using an 'end' argument, like this:
```python
print("Ik ben ")
print("Swen")
# Ik ben
# Swen

print("Ik ben ", end="")
print("Swen ", end="")
# Ik ben Swen
```

## Question 4
Here is a piece of english text. Please count the amount of 'a' symbols and the amount of 'e' symbols. Which letter appears more often? Are the amounts even or odd? Try to make your program give output like this:
```
There are 50 'a' symbols and 123 'e' symbols. 
There are more 'e' symbols.
The 'a' symbol count is even. 
The 'e' symbol count is odd. 
```

```python
text = """Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do: once or twice she had peeped into the
book her sister was reading, but it had no pictures or conversations in
it, ‘and what is the use of a book,’ thought Alice ‘without pictures or
conversations?’

So she was considering in her own mind (as well as she could, for the
hot day made her feel very sleepy and stupid), whether the pleasure
of making a daisy-chain would be worth the trouble of getting up and
picking the daisies, when suddenly a White Rabbit with pink eyes ran
close by her."""
```
Remember that this is just a (multi-line) String type. 