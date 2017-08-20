"""
    THE TIE BREAKER
    @AkhilendraGadde
"""

import random

wickets = 1
balls = 6

kb_score,nsn_score,dbv_score,hm_score = 0,0,0,0

kb_prob = [
    (0, 0.05) ,(1, 0.1) ,(2, 0.25) ,(3, 0.1) ,(4, 0.25) ,(5, 0.01) ,(6, 0.14) ,(7, 0.1) 
]
nsn_prob = [
    (0, 0.05) ,(1, 0.15) ,(2, 0.15) ,(3, 0.1) ,(4, 0.20) ,(5, 0.01) ,(6, 0.19) ,(7, 0.15) 
]

dbv_prob = [
    (0, 0.05) ,(1, 0.1) ,(2, 0.25) ,(3, 0.1) ,(4, 0.25) ,(5, 0.01) ,(6, 0.14) ,(7, 0.1) 
]
hm_prob = [
    (0, 0.1) ,(1, 0.1) ,(2, 0.25) ,(3, 0.1) ,(4, 0.25) ,(5, 0.01) ,(6, 0.14) ,(7, 0.15) 
]

lengaburu = [
    ["Kirat Boli",kb_prob,kb_score],
    ["N.S Nodhi",nsn_prob,nsn_score]
]

enchai = [
    ["DB Vellyers",dbv_prob,dbv_score],
    ["H Mamla",hm_prob,hm_score]
]

def runs_scored(batsmen):
    cdf = [
        (i, sum(k for j,k in batsmen if j < i)) for i,_ in batsmen
    ]
    return (
        max(i for r in [random.random()] for i,c in cdf if c <= r)
    )

def main():
    global wickets

    print("\n\nLengaburu innings: \n")
    Lscore = 0
    current_run = 0
    strike = 0
    
    for eachball in range(balls):

        if strike == 0:
            current_run = runs_scored(lengaburu[strike][1])
            
            if current_run == 7:
                wickets -= 1
                print(
                    "{}.{} {} is out! Lengaburu innings ends.\n Echnai need {} runs to win in 1 over."
                    .format(0,eachball+1,lengaburu[strike][0],Lscore+1)
                )
                break
            
            if current_run != 7:
                Lscore += current_run
                lengaburu[strike][2] += current_run
                print(
                    "{}.{} {} scores {} run/s !"
                    .format(0,eachball+1,lengaburu[strike][0],current_run)
                )

            if current_run == 1 or current_run == 3 or current_run == 5:                
                strike = 1
        
        elif strike == 1:
            current_run = runs_scored(lengaburu[strike][1])

            if current_run == 7:
                wickets -= 1
                print(
                    "{}.{} {} is out! Lengaburu innings ends.\n Echnai need {} runs to win in 1 over."
                    .format(0,eachball+1,lengaburu[strike][0],Lscore+1)
                )
                break
            
            if current_run != 7:
                Lscore += current_run
                lengaburu[strike][2] += current_run
                print(
                    "{}.{} {} scores {} run/s !"
                    .format(0,eachball+1,lengaburu[strike][0],current_run)
                )

            if current_run == 1 or current_run == 3 or current_run == 5:                
                strike = 0
                   
        else:
            pass
        
        if eachball+1 == balls:
            print("Lengaburu innings ends.\n Echnai need {} runs to win in 1 over.".format(Lscore+1))
    
    print("\n\nEnchai innings: \n")
    Escore = 0
    current_run = 0
    strike = 0
    
    for eachball in range(balls):

        if Escore > Lscore:
            break
        
        if strike == 0:
            current_run = runs_scored(enchai[strike][1])

            if current_run == 7:
                wickets -= 1
                print(
                    "{}.{} {} is out! Enchai innings ends."
                    .format(0,eachball+1,enchai[strike][0])
                )
                break
            
            if current_run != 7:
                Escore += current_run
                enchai[strike][2] += current_run
                print(
                    "{}.{} {} scores {} run/s !"
                    .format(0,eachball+1,enchai[strike][0],current_run)
                )

            if current_run == 1 or current_run == 3 or current_run == 5:                
                strike = 1
        
        elif strike == 1:
            current_run = runs_scored(enchai[strike][1])

            if current_run == 7:
                wickets -= 1
                print(
                    "{}.{} {} is out! Enchai innings ends."
                    .format(0,eachball+1,enchai[strike][0])
                )
                break
            
            if current_run != 7:
                Escore += current_run
                enchai[strike][2] += current_run
                print(
                    "{}.{} {} scores {} run/s !"
                    .format(0,eachball+1,enchai[strike][0],current_run)
                )

            if current_run == 1 or current_run == 3 or current_run == 5:                
                strike = 0
        
        else:
            pass
            
    if Escore > Lscore:
        print("Enchai Wins !")
    elif Lscore > Escore:
        print("Lengaburu Wins !")
    else:
        pass


if __name__ == '__main__':
    main()
