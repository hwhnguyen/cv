"""
    Powerball number generator
    ~ HN 210222 ~
"""

from random import choice

while True:
    n = input("    How many Powerball games? ")
    if n == 'q':
        break
    
    else:
        try:
            # "Clear" the console
            for i in range(100):
                print("")
            
            # How many games to generate?
            n = int(n)
            if n > 1000:
                n = 1000
                
            for i in range(n):
                # Create 35 numbered balls (1 -> 35) for the first barrel.
                std_set = [i for i in range(1,36)]
                # Create 20 numbered balls (1 -> 20) for the Powerball barrel.
                pball_set = [i for i in range(1,21)]
                
                # Initialise lists of winning numbers.
                win_std = [] # First barrel
                win_pball = [] # Powerball barrel
                
                # Randomly draw 7 balls from the first barrel.
                for i in range(7):
                    x = choice(std_set)
                    std_set.remove(x)
                    win_std.append(x)
                
                # Randomly draw one ball from the Powerball barrel.
                x_pball = choice(pball_set)
                pball_set.remove(x_pball)
                win_pball.append(x_pball)
                
                # Reformat winning numbers for convenient reading.
                # Reformatted winning numbers go in these lists.
                win_std2 = []
                win_pball2 = []
                 
                # Reformat the first 7 winning numbers to display 2 digits each.
                for i in win_std:
                    i = str(i)
                    if len(i) < 2:
                        i = "0"+i
                        win_std2.append(i)
                    else:
                        win_std2.append(i)
                
                # Reformat the winning Powerball number to display 2 digits.
                for i in win_pball:
                    i = str(i)
                    if len(i) < 2:
                        i = "0"+i    
                        win_pball2.append(i)
                    else:
                        win_pball2.append(i)
                
                # Display game results.
                pball_game = str("    ") + str(win_std2) + str("  ---  ") + str(win_pball2)
                print(pball_game.replace("'", "").replace("[", "").replace("]", ""))
                
            print(" ")
        
        # "Don't get caught."
        except ValueError:
            print("    Input an integer to continue.")
            print("    Input 'q' to quit.\n")