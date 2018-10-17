import itertools
from enum import Enum, auto

class Prices(Enum):
    SIZE = 0
    PRICE = 1
    
tall_price = 3.75
grande_price = 4.25

tax = 1.13
rem_bal = .05
max_num_of_starb= 9
prices = [["VS Cold Brew - Tall", 3.75], ["VS Cold Brew - Grande", 4.25]]

def starb_eq_v2(lin_comb):
    sum_bef_tax = 0
    for idx, comb_elem in enumerate(lin_comb):
        sum_bef_tax += comb_elem * prices[idx][1]
    
    return tax * sum_bef_tax

def starb_eq(a,b):
	return (a*tall_price + b*grande_price)	* 1.13

def get_recharge_amt(num):
    if num < 5:
        return 5
    rec_mult = int(num/5)
    if num % 5 != 0:
        rec_mult += 1
    return rec_mult * 5

def print_starb_comb(lin_comb):
    print_stmt = ""
    for idx, comb_elem in enumerate(lin_comb):
        print_stmt += "Quant -> " + str(comb_elem) + " (" + prices[idx][0] + ") " + str(prices[idx][1]) + " + "
    print(print_stmt)
    
def best_starb_comb_v2():
    best_comb_price = 999
    best_comb = []
    
    all_lin_combs = list(itertools.product(list(range(0,len(prices)+1)), repeat=len(prices)))
    for comb in all_lin_combs:
        print_starb_comb(comb)
        comb_price = starb_eq_v2(comb) - rem_bal
        rech_amt = get_recharge_amt(comb_price)
        
        print("\t price -> " + str(starb_eq_v2(comb)))
            
        print("Rech amt -> " + str(rech_amt) + "  -> rem bal -> " + str(rech_amt - comb_price))
        
        if rech_amt - comb_price < best_comb_price:
            best_comb = comb
            best_comb_price = comb_price
    
    
def best_starb_comb():
    best_comb_price = 999
    best_rech_amt = 0
    best_a = 0
    best_b = 0
    
    for a in range(1, max_num_of_starb + 1):
        b = max_num_of_starb - a
        starb_comb_price = starb_eq(a,b) - rem_bal
        #comp = (starb_comb_price * tax) - rem_bal
        rech_amt = get_recharge_amt(starb_comb_price)
        print("No. of tall's " + str(a) + " No. of grande's " + str(b) + " Rem bal = " + str(rech_amt - starb_comb_price))
        
        if rech_amt - starb_comb_price < best_comb_price:
            best_comb_price = rech_amt - starb_comb_price
            best_a = a
            best_b = b
            best_rech_amt = rech_amt
    
    print("Ideal No. of tall's " + str(best_a) + "Ideal No. of grande's " + str(best_b) + " = " + str(best_comb_price))
    print("Best rech amt " + str(best_rech_amt))
    
    for b in range(1, max_num_of_starb + 1):
        a = max_num_of_starb - b
        starb_comb_price = starb_eq(a,b) - rem_bal
        #comp = (starb_comb_price * tax) - rem_bal
        rech_amt = get_recharge_amt(starb_comb_price)
        print("No. of tall's " + str(a) + " No. of grande's " + str(b) + " Rem bal = " + str(rech_amt - starb_comb_price))
        
        if rech_amt - starb_comb_price < best_comb_price:
            best_comb_price = rech_amt - starb_comb_price
            best_a = a
            best_b = b
            best_rech_amt = rech_amt
    
    print("Ideal No. of tall's " + str(best_a) + "Ideal No. of grande's " + str(best_b) + " = " + str(best_comb_price))
    print("Best rech amt " + str(best_rech_amt))
            
#best_starb_comb()
#stuff = [1, 2, 3, 4]
#for L in range(0, len(stuff)+1):
#    for subset in itertools.permutations(stuff, L):
#        print(subset)
#print(list(itertools.permutations(list(range(1,2+1)) + list(range(1,2+1)), 2)))
comb = list(itertools.product(list(range(0,2+1)), repeat=2))
test_comb = comb[3][0] +comb[3][1]
print(starb_eq_v2([3,9]))
best_starb_comb_v2()
print("Comb length = " + str(len(comb)))
