from typing import List, Dict, Generator

#Librairies : black, mypy, pylint

def decomp(n: int, nb_bits: int) -> [bool] :
    out = [False] * nb_bits
    iter = 0
    while (n > 0) :
        out[iter] = (n%2 != 0)
        n = n//2
        iter += 1
    return out

# print(decomp(3, 4))

# > interpretation(["A", "B", "C"],[True, True, False])
# {"A": True, "B": True, "C": False}
def interpretation(voc: [str], vals: [bool]) -> [str, bool] :
    out = {}
    n = len(voc)
    for i in range(n) :
        out[voc[i]] = vals[i]
    return out

# print(interpretation(["A", "B", "C", "D"],[True, True, False, True]))

def gen_interpretations(voc: List[str]) -> [Dict[str, bool], None, None] :
    n = len(voc)
    nbInt = 2**n
    out = []
    for i in range(nbInt) :
        out.append(interpretation(voc, decomp(i, nbInt)))
    return out

# for i in gen_interpretations(["toto", "tutu", "titi"]):
#     print(i)


# > valuate("(A or B) and not(C)", {"A": True, "B": False, "C": False})
# True
def valuate(formula: str, interpretation: Dict[str, bool]) -> bool :
    return eval(formula, interpretation)

# +---+---+---+-------+
# | A | B | C | eval. |
# +---+---+---+-------+
# | T | F | F |   T   |
# +---+---+---+-------+

# print(valuate("(A or B) and not(C)", {"A": True, "B": False, "C": False}))


# > table("(A or B) and not(C)", ["A", "B", "C"])
# formule : (A or B) and not(C)
# +---+---+---+-------+
# | A | B | C | eval. |
# +---+---+---+-------+
# | F | F | F |   F   |
# | T | F | F |   T   |
# | F | T | F |   T   |
# | T | T | F |   T   |
# | F | F | T |   F   |
# | T | F | T |   F   |
# | F | T | T |   F   |
# | T | T | T |   F   |
# +---+---+---+-------+

def affiche(formula: str, voc: List[str]) -> bool :
    n = len(voc)
    print("+---+---+---+-------+")
    str1 = ""
    for val in voc :
        str1 += f"| {val} "
    str1 += "| eval. |"
    print(str1)
    print("+---+---+---+-------+")
    listeInter = gen_interpretations(voc)
    for inter in listeInter :
        str2 = ""
        for val in voc :
            str2 += f"| {inter[val]} "
        str2 += f"|   {valuate(formula, inter)}   |"
        print(str2)
    print("+---+---+---+-------+")

affiche("(A or B) and not(C)", ["A", "B", "C"])

def estValide(formula : str, voc: List[str]) -> bool :
    listeInter = gen_interpretations(voc)
    for dict in listeInter :
        if not(valuate(formula, dict)) :
            return False
    return True

print(estValide("(A or B) and not(C)", ["A", "B", "C"]))
print(estValide("A or not(A)", ["A"]))
print("")

def estContingente(formula : str, voc: List[str]) -> bool :
    mod = False
    cmod = False
    listeInter = gen_interpretations(voc)
    for dict in listeInter :
        if valuate(formula, dict) :
            mod = True
        else :
            cmod = True
    return mod and cmod

print(estContingente("(A or B) and not(C)", ["A", "B", "C"]))
print(estContingente("A or not(A)", ["A"]))
print("")

def estContradictoire(formula : str, voc: List[str]) -> bool :
    listeInter = gen_interpretations(voc)
    for dict in listeInter :
        if valuate(formula, dict) :
            return False
    return True

print(estContradictoire("(A or B) and not(C)", ["A", "B", "C"]))
print(estContradictoire("A or not(A)", ["A"]))
print("")

# voc = []
# formula = ""
# n = 15
# for i in range(n) :
#     voc.append(f"A{i}")
#     formula += f"A{i} or "
# voc.append(f"A{n+1}")
# formula += f"A{n+1}"
# print(estContingente(formula, voc))

def is_cons(f1: str, f2: str, voc: List[str]) -> bool :
    L1 = gen_interpretations(voc)
    n1 = len(L1)
    L2 = gen_interpretations(voc)
    n2 = len(L2)
    i = 0
    while i < n1 :
        if not(valuate(f1, L1[i])) :
            del(L1[i])
            n1 += -1
            i += 1
    i = 0
    while i < n2 :
        if not(valuate(f2, L2[i])) :
            del(L2[i])
            n2 += -1
            i += 1
    for inter in L1 :
        if not(inter in L2) :
            return False
    return True

print(is_cons("A", "A or B", ["A", "B"]))
