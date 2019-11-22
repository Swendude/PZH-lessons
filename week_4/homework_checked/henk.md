## Question 1:
```python
name = "Swen"

age = 26

city = "Utrecht"


if city == "Utrecht":

    if age > 18:
```
Error. Wat moet Python met de string: "This person is allowed to drink in Utrecht"?
> Correcte opmerking, ik mis alleen de volgorde van de regels

 

## Question 2:
```python
name = "Nijntje"

age = 5

city = "Nijntje country"

 

if city == "Utrecht":

if city != "Utrecht":

    print("He does not live in Utrecht so he can't drink in Utrecht")
```
 > Idem vraag 1

## Question 3:
```python
milk_needed = 1

store_has_eggs = True

if store_has_eggs == True:

    milk_bought = 6

    eggs_bought = 0
```
> `milk_needed` is niet gebruikt in de code. En de `milk_bought` verschijnt ineens in de body van de `if` statement. Mijn voorstel:

```python
store_has_eggs = True
milk_bought = 0

if store_has_eggs:
    milk_bought = 6
else:
    milk_bought = 1
```

 