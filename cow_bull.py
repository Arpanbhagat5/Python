import random
jackpot = random.randint(1000,9999)
print("jackpot is: {}".format(jackpot))
try_count = 0
while True:
    once_bulled = [0]*len(str(jackpot))
    once_cowed = [0]*len(str(jackpot))
    cows, bulls = 0,0
    user_guess = int(input("Guess: "))
    if jackpot == user_guess:
        try_count += 1
        cows = 4
        print("Well Done!! Try_count : {}".format(try_count))
        break
    else:
        jackpot_str = str(jackpot)
        for i in range(len(str(user_guess))):
            for j in range(len(str(jackpot))):
                if str(user_guess)[i] == str(jackpot)[j] and once_bulled[j] != 1:
                    if str(jackpot)[j] == str(user_guess)[j] and once_cowed != 1:
                        cows +=1
                        once_cowed[j] = 1
                    else:
                        once_bulled[j] = 1
                        bulls +=1
                    break    
        try_count += 1            
        print("Keep guessing!! Try_count : {}, Cows: {}, Bulls: {} ".format(try_count, cows, bulls))

