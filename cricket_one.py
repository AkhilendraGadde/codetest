"""
    The Last Four !
    @AkhilendraGadde
"""
import random

target = 40
wickets = 3
balls = 6*4

k_b = [(0, 0.05), (1, 0.3), (2, 0.25), (3, 0.10), (4, 0.15), (5, 0.01), (6, 0.09), (7, 0.05)]
ns_n = [(0, 0.1), (1, 0.3), (2, 0.25), (3, 0.10), (4, 0.15), (5, 0.01), (6, 0.09), (7, 0.05)]
r_r = [(0, 0.2), (1, 0.3), (2, 0.25), (3, 0.10), (4, 0.15), (5, 0.01), (6, 0.09), (7, 0.05)]
s_h = [(0, 0.3), (1, 0.25), (2, 0.05), (3, 0.0), (4, 0.05), (5, 0.01), (6, 0.04), (7, 0.3)]

kb = 0
nsn = 0
rr = 0
sh = 0

lineup = [ 
    [kb, k_b, "Kirat Boli"],
    [nsn, ns_n, "N.S Nodhi"],
    [rr, r_r, "R Rumrah"],
    [sh, s_h, "Sashi Henra"] 
]
 
def runs_per_ball(batsmen):
    cdf = [(i, sum(p for j,p in batsmen if j < i)) for i,_ in batsmen]
    return (max(i for r in [random.random()] for i,c in cdf if c <= r))

def main():

    global wickets
    ctr = 0
    ball = 0
    score = 0
    current_run = 0
    strike = 0

    for each_ball in range(balls):
        if each_ball%6 == 0:
            ctr += 1
            ball = 0
        ball += 1
        print("\nOver {} Ball {}: ".format(ctr,ball))
        
        print("On Strike : {}".format(lineup[strike][2]))

        if strike == 0:
            current_run = runs_per_ball(lineup[strike][1])
            print("Strike",strike)
            
            if current_run != 7:
                score += current_run
                lineup[strike][0] += current_run
                print("{} Scores : {}".format(lineup[strike][2],current_run))

            if current_run == 1 or current_run == 3 or current_run == 5 or ball == 6 :
                strike = 1

            if current_run == 7:
                print("{} is out".format(lineup[strike][2]))
                wickets -= 1
                spot = lineup[strike]              
                lineup.insert(strike+1,lineup[2])
                del lineup[strike]
                del lineup[2]
                lineup.append(spot)
                #strike = 1 # update
            
        elif strike == 1 :
            current_run = runs_per_ball(lineup[strike][1]) 
            print("Strike",strike)
            

            if current_run != 7:
                score += current_run
                lineup[strike][0] += current_run
                print("{} Scores : {}".format(lineup[strike][2],current_run))

            if current_run == 1 or current_run == 3 or current_run == 5 or ball == 6 :
                strike = 0
        
            if current_run == 7:
                print("{} is out".format(lineup[strike][2]))
                wickets -= 1
                spot = lineup[strike]              
                lineup.insert(strike+1,lineup[2])
                del lineup[strike]
                del lineup[2]
                lineup.append(spot)
                #strike = 0 # update
            
        print("Total score : {}".format(score))

        if wickets == 0 or score >= target:
            break         

    if score >= target:
        print("\n\nLengaluru Wins by {} wicket/s and {} balls remaining".format(wickets,balls-each_ball-1))
    else:
        print("\n\nLengaluru lost by {} runs".format(target-score))

    print(
        "\nScoreboard : \n {}* : {}\n {}* : {}\n {} : {}\n {} : {}\n"
        .format(
            lineup[0][2],lineup[0][0],
            lineup[1][2],lineup[1][0],
            lineup[2][2],lineup[2][0],
            lineup[3][2],lineup[3][0]
        )
    )
    

if __name__ == '__main__':
    main()