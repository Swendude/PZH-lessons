#  Question 1:
# In which order will these lines 'execute'?
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
 ```
 
# Question 2:
# The same as Question 3 but with the following variables
```python
name = "Nijntje"
age = 5
city = "Nijntje country"
```

# Question 3:
Programmer humour is some of the best around. A famous joke among developers is:

- My wife said:
- "Please go to the store and buy a carton of milk and if they have eggs, get six."
- I came back with 6 cartons of milk 
- She said: 
- "Why in the hell did you buy six cartons of milk"
- Husbands response:
- "They had eggs"" 

Try to implement the logic in this joke, what did the husband or wife understand wrong?
TIP: A good starting point is to declare variabales to model the "state of the world". i.e. store_has_eggs = True

# Additional work
- Study LPTHW Exercise 29, 30, 31