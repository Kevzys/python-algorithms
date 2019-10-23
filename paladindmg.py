from random import randint

def roller(damage_calc, dice, number):
    #parameters: total_damage: updates total damage done so far
    #            dice: which dice to roll for
    #            number: how many times to roll
    #return:     total_damage: updated damage returned
    for x in range(number):
        roll = int(randint(1, dice))
        print("rolled " + str(roll) + " for dice: D"+str(dice))
        damage_calc+=  roll#fix line??? Math random
    return damage_calc


total_damage = 0
D8 = 8
D6 = 6
D4 = 4
STRENGTH = 5 #Base damage
WEAPON_DAMAGE = 0 #4d6 (for my current weapon)
print("Paladin damage calc")

#Add STRENGTH bc yes
total_damage += STRENGTH
#Add improved divine smite (because it is always added)
total_damage = roller(total_damage, D8, 1) #1 time because only added once
#Add weapon damage
total_damage = roller(total_damage, D4, 4) #4 times because fire sword is blessed
print(total_damage)
#Add smite damage based off level
x = input("Smite? (y/n)")
if x == "y":
    smite_level = int(input("Enter smite level (1-3)"))
    total_damage = roller(total_damage, D8, smite_level+1) #Calls roller function that will generate the random rolls

isUndead = input("Is the enemy undead? (y/n)")
if isUndead == "y":
    total_damage = roller(total_damage, D8, 1) # INPUT 1 because only need to roll once

print("Total damage done to monster is: "+str(total_damage))
