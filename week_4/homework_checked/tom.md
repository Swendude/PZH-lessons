```python
In which order will these lines 'execute'? 

 1. name = "Swen"
 2. age = 26
 3. city = "Utrecht"
 4.  
 5. if city == "Utrecht":
 6.     if age > 18:
 7.         "This person is allowed to drink in Utrecht"
 8.     if age < 18:
 9.         "This person is not allowed to drink in Utrecht"
10. if city != "Utrecht":
11.    print("He does not live in Utrecht so he can't drink in Utrecht")

#Answer:
#1, 2, 3, 5, 6, 7, 8, 10


# In which order will these lines 'execute'?

 1. name = "Nijntje"
 2. age = 5
 3. city = "Nijntje country"
 4.  
 5. if city == "Utrecht":
 6.     if age > 18:
 7.         "This person is allowed to drink in Utrecht"
 8.     if age < 18:
 9.         "This person is not allowed to drink in Utrecht"
10. if city != "Utrecht":
11.    print("He does not live in Utrecht so he can't drink in Utrecht")

# 1, 2, 3, 5, 10, 11



 1. store_has_eggs = True
 2.
 3. if store_has_eggs == True
 4.     "Buy six cartons of milk"
 5. if store_has_eggs == False
 6.     "Buy one carton of milk"

#De logica is dat de vrouw zei dat als de winkel eieren zou hebben, #de man zes van het 'onderwerp' mee moest nemen, dat is 'a carton #of milk'.
#Ze bedoelde te zeggen dat als er eieren waren, de man zes eieren #mee moest nemen

 1. store_has_eggs = True
 2.
 3. if store_has_eggs == True
 4.     "Buy 1 carton of milk and six eggs"
 5. if store_has_eggs == False
 6.     "Buy 1 carton of milk"
```

> Goed gedaan! Zelfde feedback als Erik en Fiona:
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