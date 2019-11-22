```python
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

# Answer: from top to bottom. An "if" is only executed when True. 
# In this case line 5 is executed because the variable city is equal to Utrecht. Python moves on to line 6.
# Since line 6 is alto True, because 26 > 18, this "if" is also executed and thus line 7 is the final result.
# In this case lines 8, 9, 10 & 11 are not excecuted because they are False.

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

# Answer: still top to bottom :). In this case the first if-statement (line 22) is False.
# Therefore lines 23 till 26 are not executed at all. Python moves on to line 27.
# The if-statement on line 27 is True because the var city does not equal "Utrecht". Therefore line 28 is executed.
# The string on line 28 is printed.

# Q3
# The wife wanted te husband to get 1 carton of milk and six eggs if they have them.
# What the husband understood:
store_has_eggs = True

if store_has_eggs == True:
    buy = "buy 6 milk"
else:
    buy = "buy 1 milk"

print(buy)
```

> Good job, zelfde suggestie als bij Fiona:
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