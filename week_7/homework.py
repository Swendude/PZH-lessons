# You have been hired by the startup www.fruits.com to help them manage the store using your awesome python skills
# Try to complete the following assignments to help www.fruits.com grow into an unicorn startup

# The previous developer left behind a mess and the stock information is completly fucked. 
# The current stock information in the system is represented as a list of dictionaries where every dictionary represents a fruit delivery from the supplier

# Here is the current stock:
stock = [{"type":"banana", "amount":500, "buy-price":0.3, "sell-price":0.6},
    {"type":"pears", "amount":100, "buy-price":0.4, "sell-price":0.45},
    {"type":"apples", "amount":150, "buy-price":1, "sell-price":1.45},
    {"type":"pineapples", "amount":50, "buy-price":3, "sell-price":3.15}]   

# Assignment 1: The manager informs you that the selling price of apples is actually 1.55, please change it in the stock definition

# Asignment 2: Another delivery comes in, we got some nice coconuts, 25 of them. The managers provides the following pricing info:
    # coconut buy price: 5
    # coconut sell price: 5.25

# Assignment 3: The manager asks you to count the total amount of fruits available at www.fruits.com, please provide this information

# Assignment 4: A group of oerangatangs enters the shop, they steall al the bananas. Update the stock information to reflect this incident.

# Assignment 5: The manager is still angry over the monkeys. He asks how much money did they lose? 

# Assignment 6: A customer buys the following fruits: 5x pineapple, 10x apples, 1 pear. How much profit did the store make? Also update the stock information

# Assignment 7: Global warming keeps on going, the price for fruits is 10% higher. Reflect this price change in the stock information

# Assignment 8: www.fruits.com experienced a lot of bad luck, however over at the competition (www.fruits.net) bussines is booming. 
# They decide to buy www.fruits.com, their IT systems need to be integrated. Please add the old remaining stock to the stock information from fruits.net
# Be aware: This is a different system so the field names will not match. This is called a 'data migration' and is a pain in the ass.

stock_fruitsnet = [{"Type":"Banana", "Quantity":500, "Buyprice":0.1, "Sellprice":0.6},
    {"Type":"Coconut", "Quantity":100, "Buyprice":4, "Sellprice":6}]

