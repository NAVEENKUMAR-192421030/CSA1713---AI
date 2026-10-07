from itertools import permutations

def solve_cryptarithm():
    letters = "SENDMORY"
    
    for p in permutations(range(10), len(letters)):
        d = dict(zip(letters, p))

        if d['S'] == 0 or d['M'] == 0:
            continue

        SEND = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
        MORE = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
        MONEY = (10000*d['M'] + 1000*d['O'] +
                 100*d['N'] + 10*d['E'] + d['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found:")
            print("SEND  =", SEND)
            print("MORE  =", MORE)
            print("MONEY =", MONEY)
            print()
            print("Letter Mapping:")
            
            for letter in sorted(d):
                print(letter, "=", d[letter])

            return

    print("No solution found.")

solve_cryptarithm()
