# Author: Sunil Mann
# Date: September 22, 2019

# This program acts as a 1v1 Dungeons and Dragons 5th Edition encounter simulator. The program only works for 1 melee attack per turn. 
import random
import replit
# randomize a monster
monsterList = ["Goblin", "Ogre", "Orc", "Bugbear", "Hobgoblin","Hydra", "Dark Elf", "High Elf", "Dwarf", "Gnome"]
diceList = [4,6,8,10,12]
#   give it an Armor Class, Health Points and a name
monsterName = random.choice(monsterList)
monsterAC = random.randrange(1,21,1)
monsterHP = random.randrange(10,40,1)
monsterDamage = random.choice(diceList)
monsterDiceAmount = random.randrange(1,5,1)
# ask for your characters name
userName = input("Hi and let's play some Dungeons and Dragons\n\nWhat is your character's name? ")

# ask for your Armor Class
userAC = int(input("\nWhat is your Armor Class? "))

# ask for your Health Points
userHP = int(input("\nWhat is your current HP? "))

# ask for weapon proficencies
proficency = input("\nDo you have proficency with your current weapon? ")
userBonus = 0
statBoost = 0
# enter your proficency bonus
if proficency == "no":
  bonus = int(input("\nWhat is your proficency bonus? "))

  # ask if it is a finesse weapon
  finesse = input("\nIs this a finesse weapon? ").lower().strip(".!?")

  # use an if statement for either the dexterity or strength bonus
  if finesse == "yes":
    # ask for dex or strength bonus
    statBoost += int(input("\nWhat is your dexterity bonus? "))
  else:
    statBoost += int(input("\nWhat is your strength bonus? "))

  userBonus = bonus + statBoost
else:
  bonus = 0
# ask for the damage the weapon does
userDamage = int(input("\nWhich dice do you use for the damage?  ".strip("?dD")))

# ask how many of that dice you use for the weapon
userDiceAmount = int(input("\nHow many dice do you use for the damage? "))

print("Ok let's fight!\n")

replit.clear()

print("You are walking on the Scott Road when out of nowhere a " + monsterName + " appears! \nHe is ready for a fight. \nYou draw your weapon and prepare to duel.")
# roll intiative
monsterInitiative = random.randrange(1,20,1)

# get the user's initiative
userInitiative = random.randrange(1,20,1)
inBonus = int(input("What is your initiative bonus? ").strip("+"))
userInitiative += inBonus

# check intiative to decide turn order
attackFirst = False
if (monsterInitiative < userInitiative):
  attackFirst = True
  print("You will go first.")
else:
  print("The " + monsterName + " will go first.")

monsterAttack = 0
userAttack = 0

# time to play out the fight
if attackFirst:
  # have a loop that goes until someone dies
  while(monsterHP > 0 and userHP > 0):

    #resets the overall turn damage for the user and the monster
    userTurnDamage = 0
    monsterTurnDamage = 0
    # roll a d20 to find out the users Attack
    userAttack = random.randrange(1,21,1) + userBonus
    # check it against the monster's AC
    if userAttack > monsterAC:
      #hit the monster for some damage
      #add in proficency to damage
      for i in range(userDiceAmount):
        userTurnDamage += random.randrange(1,userDamage+1,1)
        userTurnDamage += statBoost
      
      # subtract the damage done to the overall HP
      # tell the user how much health is left on the person who got hit
      print("You use your weapon and hit the enemy\n")
      monsterHP = monsterHP - userTurnDamage
      print("Your attack does " + str(userTurnDamage) + " damage.")
      print("The " + monsterName + " has " + str(monsterHP) + " HP left.")
    
    else:
      print("Big swing but an even bigger miss on the atttack.\n")
    # roll a d20 to find out the monsters attack
    input("Enter anything to end your turn. ")
    print("\n")
    monsterAttack = random.randrange(1,21,1)
    # check it against the user's AC
    if monsterAttack > userAC:
      #hit the user for some damage
      # more or less this is just the inverse of the user turn
      for i in range(monsterDiceAmount):
        monsterTurnDamage += random.randrange(1,monsterDamage+1,1)

      print("The " + monsterName + " hits you.\n")
      userHP = userHP - monsterTurnDamage
      print("You take " + str(monsterTurnDamage) + " damage.")
      print("You know have " + str(userHP) + " HP left.")
    else:
      print("\nThe monster swings for a big hit but you easily dodge it.")
    print ("\nThe monster's turn is over.")
    input("\nInput anything to continue. ")
    print("\n")

else:
   # have a loop that goes until someone dies
  while(monsterHP > 0 and userHP > 0):

    #resets the overall turn damage for the user and the monster
    userTurnDamage = 0
    monsterTurnDamage = 0

    monsterAttack = random.randrange(1,21,1)
    # check it against the user's AC
    if monsterAttack > userAC:
      #hit the user for some damage
      # more or less this is just the inverse of the user turn
      for i in range(monsterDiceAmount):
        monsterTurnDamage += random.randrange(1,monsterDamage+1,1)
      print("The " + monsterName + " hits you.\n")
      userHP = userHP - monsterTurnDamage
      print("You take " + str(monsterTurnDamage) + " damage.")
      print("You know have " + str(userHP) + " HP left.")
    else:
      print("\nThe monster swings for a big hit but you easily dodge it.")
    print ("\nThe monster's turn is over.")
    input("\nInput anything to continue. ")
    print("\n")

    # roll a d20 to find out the users Attack
    userAttack = random.randrange(1,21,1) + userBonus
    # check it against the monster's AC
    if userAttack > monsterAC:
      #hit the monster for some damage
      # TODO add in proficency to damage
      for i in range(userDiceAmount):
        userTurnDamage += random.randrange(1,userDamage+1,1)
      
      print("You use your weapon and hit the enemy\n")
      monsterHP = monsterHP - userTurnDamage
      print("Your attack does " + str(userTurnDamage) + " damage.")
      print("The " + monsterName + " has " + str(monsterHP) + " HP left.")
    
    else:
      print("Big swing but an even bigger miss on the atttack.")
    # roll a d20 to find out the monsters attack
    input("Enter anything to end your turn. ")

# TODO fix the ending dialogues
# give a message summing up how the battle went.
if(userHP >= 0 and monsterHP <= 0):
  print("BOOM \nClean hit on the " + monsterName + ". You stand there. The sight of victory. You quickly search the body. \nIt turns out it was just a mimic pretending to be a " + monsterName + ". \nYou walk away sour that you lost out on a good looting.")
elif (userHP <= 0 and monsterHP >= 0):
  print("CRASH\nYour whole body is too weak to get up. \nYou can't feel anything. \nAll you can see is the " + monsterName + " standing over your body. \nYou see it go back to it's true form. \nYou just got beat by a table.")
else:
  print("Something overcame you. \nYou feel a complete out of body experience \nPOOF \nHmmmmmmm. I guess it was a dream.") 

# sendoff message
print("Thank you for playing and hopefully you come back for another game.")