import random
dice_result=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(dice1,dice2)
    dice_result.append(dice1+dice2)

print(dice_result)