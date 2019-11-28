fruits = ['Tomato', 'Pumpkin', 'Cucumber', 'Eggplant']
animals = ['Dog', 'Whale', 'Crow', 'Snake']
mammals = ['Dog', 'Whale', 'Cat']
 
print(fruits[2])
print(fruits[-1])
print(fruits[2 + 1])
# print(animals[5])
print(animals[0] in mammals)
print(fruits[1:2])
print(fruits[:4])
print(fruits[-2:] )
print(animals[-5:])
print(fruits[::2])
print(fruits[::3])
print(fruits[1::2])
print(fruits[2:3] in fruits[2:])
print(fruits.append("Orange"))

print(fruits)w

fruits.sort()
print(fruits)
fruits[1:]
print(fruits)
schaap = fruits.pop()
print(fruits)
fruits.pop(len(fruits) - 1)
print(fruits)
fruits.append(schaap)
print(fruits)
if "Eggplant" in fruits:
    fruits.remove("Eggplant")
    fruits.sort()
else:
    fruits.reverse()
print(fruits)

x = 1
y = 2
