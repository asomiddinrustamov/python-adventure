####################################
#        Author: Amber Lee         #
# Email: cryptoboxcomics@gmail.com #
#      Info: A choose-your-own     #
#          adventure game          #
####################################

player_name = ""
player_health = 100
player_money = 50
player_species = "Human"
player_weapons = []
player_items = []

####################################
#            Game Start!           #
####################################

###         Introduction         ###

print()
print()
print("   ####################################################")
print("   # Hello! This is a choose-your-own-adventure game. #")
print("   #  You are a hero trying to save your kingdom of   #")
print("   #       Kanbal from the evil King Rogsam.          #")
print("   ####################################################")
print()
print()

while(player_name == ""):
    player_name = input("What is your name, Hero? : ")

print()
print("Hi, " + player_name + "! You are our hero and savior! Please save the Kanbalese mountain people from the evil King Rogsam.")
print("You start off with no weapons or items, but if you make the right choices, you might survive.")
print()

#    ---Section Author: <your name>---   #
print("You pass by a traveler who looks injured by the woods. What do you do?")
print("1. Ignore him")
print("2. Try to help him")
decision = input("Pick a number: ")
print()
if (decision == "1"):
    print("You try to leave, but trip over a rock and hit your head!")
    player_health = player_health - 10
    print("Your health now: ")
    print(player_health)
elif (decision == "2"):
    print("He appreciates that you helped him, and he gives you a potion! A potion heals 20 health points.")
    player_items.append("Potion")
    print("Your items now: ")
    print(player_items)
#            ---section end---           #

# Section author: Balsa                  #
print("The Kanbalese police stop you and try to collect taxes from you! What do you do!")
print("1. Fight the police")
print("2. Just pay your taxes")
decision = ""
while(decision == "" or decision > "2" or decision == 0 ):
    decision = input("Pick a number")
    if (decision == "1"):
        print("You got arrested! Game over!")
        exit()
    elif (decision == "2"):
        print("You lost all your money!")
        player_money = player_money * 0.8
        print("The money you have left is:")
        print(str(player_money))
#  End section #

# CoronaVirus
print("################ c o r o n a v i r u s ################")
print("You are in land of CoronaVirus")
print("I suggest you to buy some weapons to fight with them")
print("We got 2 rolls of toilet papers and 2 galons of water in stock, but NO hand sanitizers.\nWhat do you want to buy?")
print("Please enter 1 for toilet papers and 2 for waters")
decision = ""
while(decision == '' or decision > "2" or decision == "0"):
    decision = input("pick a number")
    if (decision == "1"):
        print(" [][] you got your weapon, but lost all your money. So Just wait for help. GAME OVER")
        player_weapons.append("toilet_papers [][]")
        print("new weapon: " + str(player_weapons))
        player_money = player_money * 0.01
        print("Money: " + str(player_money))

        exit ()
    elif (decision == "2"):
        print("you got water, but you still got some money")
        player_money = player_money * 0.5
        print("good luck!")
