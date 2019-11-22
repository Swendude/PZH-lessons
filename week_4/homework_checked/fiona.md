```python
# Question 1:
# In which order will these lines 'execute'?
name = "Swen"
age = 26
city = "Utrecht"
 
if city == "Utrecht":
    if age > 18:
        "This person is allowed to drink in Utrecht"
    if age < 18:
        "This person is not allowed to drink in Utrecht"
if city != "Utrecht":
    print("He does not live in Utrecht so he can't drink in Utrecht")

# order of execution: 3, 4, 5, 7, 8, 9 (no output)

# Question 2:
# The same as Question 3 but with the following variables
name = "Nijntje"
age = 5
city = "Nijntje country"

if city == "Utrecht":
    if age > 18:
        "This person is allowed to drink in Utrecht"
    if age < 18:
        "This person is not allowed to drink in Utrecht"
if city != "Utrecht":
    print("He does not live in Utrecht so he can't drink in Utrecht")

# order of execution: 19, 20, 21, 23, 28, 29 (includes output)

# Question 3:
# Programmer humour is some of the best around. A famous joke among developers is:
# My wife said:
# "Please go to the store and buy a carton of milk and if they have eggs, get six."
# I came back with 6 cartons of milk
# She said:
# "Why in the hell did you buy six cartons of milk"
# Husbands response:
# "They had eggs""
# Try to implement the logic in this joke, what did the husband or wife understand wrong?
# TIP: A good starting point is to declare variables to model the "state of the world". i.e. store_has_eggs = True

store_has_eggs = True

if  store_has_eggs == True:
    print("buy 6 cartons of milk")
else:
    print("buy 1 carton of milk")
# or
store_has_eggs = False

if  store_has_eggs == True:
    print("buy 6 cartons of milk")
else:
    print("buy 1 carton of milk")

# Study LPTHW Exercise 29, 30, 31 (p. 136, 138, 142)
```
> Goed gedaan! Kleine verbetering voor vraag drie zou zijn:
```python
store_has_eggs = True
milk_bought = 0
if  store_has_eggs == True:
    milk_bought = 6
else:
    milk_bought = 1

print(f"buy {milk_bought} carton(s) of milk")
```
> Hierdoor is je code 'DRY' (Don't Repeat Yourself!)