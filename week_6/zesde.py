# import random

# # deelnemer_list = [['Erik', 'Tom', 'Nicky', 'Fiona'], [1,2,3], "Aap"]
# # # print(random.choice(deelnemer_list))


# # for foo in enumerate(deelnemer_list):
# #     print(foo)

# # # print(list(enumerate(deelnemer_list)))

# heroes = ["King Arthur", "Robin Hood", "Batman", "Gandalf", "Bob Marley"]
# baddies = ["Sauron", "The Joker", "The Sherrif", "Prins John"]
# locations = ["Sherwood Forest", "Middle-Earth", "Gotham", "The Round Table"]
# events = ["total destruction", "a volcanic eruption", "an earthquake"]

# chosen_hero = random.choice(heroes)
# chosen_baddie = random.choice(baddies)
# chosen_location = random.choice(locations)
# chosen_event = random.choice(events)

# story_template = f"There once was {chosen_hero}, {chosen_hero} has to defeat {chosen_baddie} in order to save {chosen_location} from {chosen_event}."
# print(story_template)

string_nummers = open("input.txt").readlines()
nummers = []
for string_nummer in string_nummers:
    nummers.append(int(string_nummer))
print(nummers)