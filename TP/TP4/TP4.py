from typing import Callable
import random
# [IA02] TP feuille 4 – Jouons au morpion
# Information	Valeur
# Auteur	Sylvain Lagrue (sylvain.lagrue@utc.fr)
# Licence	Creative Common CC BY-SA 3.0
# Version document	0.0.2
# I. Présentation du sujet
# L'objectif est de ce sujet est d'implémenter les règles du Tic-Tac-Toe, une interface textuelle pour pouvoir jouer et enfin différents agnts artificiels, le tout en Python.

# Les règles sont accessibles ici : https://fr.wikipedia.org/wiki/Tic-tac-toe

# Un site sympathique si vous êtes intéressés par les mathématiques de ce jeu : https://zestedesavoir.com/billets/3672/combien-y-a-t-il-de-positions-au-morpion/

# II. Implémentation des règles
# Structures de données
# On représentera la grille de jeu à l'aide de tuples de tuples d'entier. L'entier 0 représente une case vide, 1 représente une case marquée par X et 2 une case marquée par O. Cette grille représente un état du jeu. L'objectif est de travailler avec des représentaion non-mutables.

# Une action est un tuple des coordonnées de la case. Un joueur est représenté par un entier.

# # Quelques structures de données

# Grid = tuple[tuple[int, ...], ...]
# State = Grid
# Action = tuple[int, int]
# Player = int
# Score = float
# Strategy = Callable[[Grid, Player], Action]

# # Quelques constantes
# DRAW = 0
# EMPTY = 0
# X = 1
# O = 2
# Préliminaires
# Afin de faciliter les changements entre représentations mutables et non mutables de la grille (ex: quand vous aurez besoin de changer l'état du jeu après une action), écrire les fonctions suivantes.

# def gridTupleToGridList(grid: Grid) -> list[list[int]]
# def gridListToGridTuple(grid: list[list[int]]) -> Grid
# Règles de base
# Écrire les fonctions suivantes implémentant les règles du jeu.

# def line(grid: State, player: Player) -> bool
# line renvoie vrai si la grille grid contient une ligne pleine du joueur player, faux sinon. Ne pas hésiter à décomposer cette fonction en plusieurs sous-fonctions…

# def final(grid: State) -> bool:
# final renvoie vraie si la grille grilleest un état final, c'est à dire si un joueur a gagné ou s'il n'est plus possible de marquer une case.

# def score(grid: State) -> float
# score est une fonction qui étant donné un état final, retourne le score du jeu.

# def pprint(grid: State)
# pprint est une fonction qui étant donnée un état fait une joli affichage de la grille. Par exemple :

# O 0 X 
# X X X 
# 0 O O
# def legals(grid: State) -> list[Action]
# legals est une fonction qui étant donné un état et joueur, renvoie l'ensemble des actions légales pour ce joueur.

# def play(grid: State, player: Player, action: Action) -> State
# play est une fonction qui étant donné un état, un joueur et l'action jouée par ce joueur, retourne le nouvel état de jeu.

# III. Ajout de premiers joueurs et boucle de jeu
# def strategy(grid: State, player: Player) -> Action
# Une strategie est une une fonction qui étant donné un état et un joueur renvoie l'action choisie par ce joueur.

# Joueur humain
# Voici un exemple de joueur humain, c'est-à-dire une interface texte permettant de jouer.

# def strategy_brain(grid: Grid, player: Player) -> Action:
#     print("à vous de jouer: ", end="")
#     s = input()
#     print()
#     t = ast.literal_eval(s)

#     return t
# Boucle de jeu
# def tictactoe(strategy_X: Strategy, strategy_O: Strategy, debug: bool = False) -> Score
# Écrire une fonction tictactoe qui étant données deux stratégies s'occupe de la boucle de jeu, du gagnant et renvoie le score à la fin du jeu.

# Joueur first_action
# def strategy_first_legal(grid: State, player: Player) -> Action
# Ce joueur joue toujours la première action légale disponible.

# Joueur aléatoire
# def strategy_random(grid: State, player: Player) -> Action
# Ce joueur joue au hasard l'une des actions légales disponibles.

# IV. Joueurs intelligents
# Minmax de base
# def minmax(grid: State, player: Player) -> float
# Écrire la fonction minmax qui étant donné un état de jeu renvoie le score optimal de la partie.

# Minmax avec une action
# Écrire la fonction minmax qui étant donné un état de jeu renvoie sous forme de tuple l'action amenant au score optimal de la partie et ce score.

# minmax_action(grid: State, player: Player, depth: int = 0) -> tuple[float, Action]
# En déduire la fonction suivante.

# def strategy_minmax(grid: Grid, player: Player) -> Action:
# Minmax indéterministe avec choix d'actions
# Écrire la fonction minmax qui étant donné un état de jeu renvoie dans un tuple les actions amenant au score optimal de la partie et ce score.

# def minmax_actions(
#     grid: State, player: Player, depth: int = 0
# ) -> tuple[float, list[Action]]
# Utiliser cette fonction pour créer un minmax indéterministe.

# def strategy_minmax_random(grid: Grid, player: Player) -> Action
# Annexes
# Quelques grilles prédéfinies

# EMPTY_GRID: Grid = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
# GRID_0: Grid = EMPTY_GRID
# GRID_1: Grid = ((0, 0, 0), (0, X, O), (0, 0, 0))
# # (0, 0, 0),
# # (0, X, O),
# # (0, 0, 0))

# GRID_2: Grid = ((O, 0, X), (X, X, O), (O, X, 0))
# #((O, 0, X),
# # (X, X, O),
# # (O, X, 0)

# GRID_3: Grid = ((O, 0, X), (0, X, O), (O, X, 0))
# #((O, 0, X),
# # (0, X, O),
# # (O, X, X))

# GRID_4: Grid = ((0, 0, 0), (X, X, O), (0, 0, 0))
# #((0, 0, 0),
# # (X, X, O),
# # (0, 0, 0))

# Afin de faciliter les changements entre représentations mutables et non mutables de la grille (ex: quand vous aurez besoin de changer l'état du jeu après une action), écrire les fonctions suivantes.
# def gridTupleToGridList(grid: Grid) -> list[list[int]]
# def gridListToGridTuple(grid: list[list[int]]) -> Grid

# Quelques structures de données

Grid = tuple[tuple[int, ...], ...]
State = Grid
Action = tuple[int, int]
Player = int
Score = float
Strategy = Callable[[Grid, Player], Action]

# Quelques constantes
DRAW = 0
EMPTY = 0
X = 1
O = 2

# Annexes

EMPTY_GRID: Grid = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
GRID_0: Grid = EMPTY_GRID
GRID_1: Grid = ((0, 0, 0), (0, X, O), (0, 0, 0))
# (0, 0, 0),
# (0, X, O),
# (0, 0, 0))

GRID_2: Grid = ((O, 0, X), (X, X, O), (O, X, 0))
#((O, 0, X),
# (X, X, O),
# (O, X, 0)

GRID_3: Grid = ((O, 0, X), (0, X, O), (O, X, 0))
#((O, 0, X),
# (0, X, O),
# (O, X, X))

GRID_4: Grid = ((0, 0, 0), (X, X, O), (0, 0, 0))
#((0, 0, 0),
# (X, X, O),
# (0, 0, 0))

# Fonctions

def gridTupleToGridList(grid: Grid) -> list[list[int]] :
    return [list(row) for row in grid]

def gridListToGridTuple(grid: list[list[int]]) -> Grid :
    return tuple(tuple(row) for row in grid)

def line(grid: State, player: Player) -> bool :
    for row in grid : # Lignes
        if all([cell == player for cell in row]) :
            return True
    for col in range(3) : # Colonnes
        if all([grid[row][col] == player for row in range(3)]) :
            return True
    if all([grid[i][i] == player for i in range(3)]) : # Diagonale
        return True
    if all([grid[i][2-i] == player for i in range(3)]) : # Anti-diagonale
        return True
    return False

def final(grid: State) -> bool:
    return any([line(grid, player) for player in [X, O]]) or all([cell != EMPTY for row in grid for cell in row])

# Jeu à somme nulle
def score(grid: State) -> float :
    if line(grid, X) :
        return 1
    if line(grid, O) :
        return -1
    return DRAW

def pprint(grid: State) :
    for row in grid :
        for cell in row :
            print("X" if cell == X else "O" if cell == O else " ", end=" ")
        print()

# grid = ((X, O, X), (O, X, O), (X, O, X))
# grid2 = ((O, X, O), (X, O, X), (O, X, EMPTY))
# pprint(grid)
# print(score(grid))
# pprint(grid2)
# print(score(grid2))

def legals(grid: State) -> list[Action] :
    return [(row, col) for row in range(3) for col in range(3) if grid[row][col] == EMPTY]

def play(grid: State, player: Player, action: Action) -> State :

    # On transforme la grille en liste pour pouvoir la modifier
    grid = gridTupleToGridList(grid)

    row, col = action
    grid[row][col] = player
    return gridListToGridTuple(grid)

def tictactoe(strategy_X: Strategy, strategy_O: Strategy, debug: bool = False) -> Score :
    grid = ((EMPTY, EMPTY, EMPTY), (EMPTY, EMPTY, EMPTY), (EMPTY, EMPTY, EMPTY))
    player = X
    turn = 0
    while not final(grid) :
        
        action = strategy_X(grid, player) if player == X else strategy_O(grid, player)
        grid = play(grid, player, action)
        
        if player == X :
            player = O
        else :
            player = X
        if debug :
            pprint(grid)
            print("---------------------------------")
    return score(grid)

def strategy_first_legal(grid: State, player: Player) -> Action :
    return legals(grid)[0]

def strategy_random(grid: State, player: Player) -> Action :
    return random.choice(legals(grid))

# Minmax

def minmax(grid: State, player: Player) -> float :
    if final(grid) :
        return score(grid)
    if player == X :
        return max([minmax(play(grid, player, action), O) for action in legals(grid)])
    else :
        return min([minmax(play(grid, player, action), X) for action in legals(grid)])
    
def minmax_action(grid: State, player: Player, depth: int = 0) -> tuple[float, Action] :
    if final(grid) :
        return score(grid), None
    if player == X :
        return max([(minmax(play(grid, player, action), O), action) for action in legals(grid)])
    else :
        return min([(minmax(play(grid, player, action), X), action) for action in legals(grid)])

def strategy_minmax(grid: Grid, player: Player) -> Action :
    return minmax_action(grid, player)[1]

# print(f"Score = {tictactoe(strategy_minmax, strategy_minmax, True)}")


def minmax_actions(grid: State, player: Player, depth: int = 0) -> tuple[float, list[Action]]:
    if depth == 0 or final(grid):
        return score(grid), []
    if player == X:  # maximizing player
        best_value = float('-inf')
        best_actions = []
        for action in legals(grid):
            v, _ = minmax_actions(play(grid, player, action), O, depth - 1)
            if v > best_value:
                best_value = v
                best_actions = [action]
            elif v == best_value:
                best_actions.append(action)
        return best_value, best_actions
    else:  # minimizing player
        best_value = float('inf')
        best_actions = [action]
        for action in legals(grid):
            v, _ = minmax_actions(play(grid, player, action), X, depth - 1)
            if v < best_value:
                best_value = v
                best_actions.append(action)
            elif v == best_value:
                best_actions.append(action)
        return best_value, best_actions
    
def strategy_minmax_random(grid: Grid, player: Player) -> Action :
    return random.choice(minmax_actions(grid, player)[1])

print(f"Score = {tictactoe(strategy_minmax_random, strategy_minmax, True)}")