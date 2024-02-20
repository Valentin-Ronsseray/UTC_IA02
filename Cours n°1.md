# IA02 : Logique propositionnelle ^toc

- [[#IA02 : Logique propositionnelle ^toc|IA02 : Logique propositionnelle]]
	- [[#I. Introduction|I. Introduction]]
		- [[#I.1. But de la logique|I.1. But de la logique]]
			- [[#I.1.1. Période classique (Aristote, Platon, les péripatéticiens etc)|I.1.1. Période classique (Aristote, Platon, les péripatéticiens etc)]]
			- [[#I.1.2. Période moderne|I.1.2. Période moderne]]
			- [[#I.1.3. Les trois formes de raisonnements|I.1.3. Les trois formes de raisonnements]]
					- [[#Exemples :|Exemples :]]
			- [[#I.1.4. Applications|I.1.4. Applications]]
			- [[#I.1.5. La logique propositionnelle|I.1.5. La logique propositionnelle]]
	- [[#II. Le langage|II. Le langage]]
					- [[#Remarque|Remarque]]
				- [[#Définition (*formules propositionnelles bien formées*)|Définition (*formules propositionnelles bien formées*)]]
		- [[#II.2. Priorité des opérateur|II.2. Priorité des opérateur]]
		- [[#II.3. Littéral|II.3. Littéral]]
				- [[#Définition (*littéral*)|Définition (*littéral*)]]
		- [[#II.4. Représentation sous formes de graphes|II.4. Représentation sous formes de graphes]]
					- [[#Exemple|Exemple]]
					- [[#Exemple|Exemple]]
					- [[#Note|Note]]
	- [[#III. Sémantique|III. Sémantique]]
		- [[#III.1. Interprétation|III.1. Interprétation]]
				- [[#Définition (*Interprétation*)|Définition (*Interprétation*)]]
					- [[#Remarque|Remarque]]
					- [[#Note|Note]]
		- [[#III.2. Valuation|III.2. Valuation]]
				- [[#Définition (*valuation*)|Définition (*valuation*)]]
					- [[#Remarque|Remarque]]
					- [[#Note|Note]]
				- [[#Définition (*modèle et contre-modèle*)|Définition (*modèle et contre-modèle*)]]
				- [[#Définition|Définition]]
		- [[#III.3. Calculer la validité d'une formule|III.3. Calculer la validité d'une formule]]
#Cours #IA02 #P24
- [[#IA02 : Logique propositionnelle ^toc|IA02 : Logique propositionnelle]]
	- [[#I. Introduction|I. Introduction]]
		- [[#I.1. But de la logique|I.1. But de la logique]]
			- [[#I.1.1. Période classique (Aristote, Platon, les péripatéticiens etc)|I.1.1. Période classique (Aristote, Platon, les péripatéticiens etc)]]
			- [[#I.1.2. Période moderne|I.1.2. Période moderne]]
			- [[#I.1.3. Les trois formes de raisonnements|I.1.3. Les trois formes de raisonnements]]
					- [[#Exemples :|Exemples :]]
			- [[#I.1.4. Applications|I.1.4. Applications]]
			- [[#I.1.5. La logique propositionnelle|I.1.5. La logique propositionnelle]]

## I. Introduction

### I.1. But de la logique
Formaliser mathématiquement le raisonnement humain

#### I.1.1. Période classique (Aristote, Platon, les péripatéticiens etc)

- Analyser des raisonnements et de l'argumentation (dialectique vs rhétorique)
- 2 types de raisonnements fallacieux : le paralogisme et le sophisme
- Objectif : la recherche de la vérité

#### I.1.2. Période moderne

- Donner un sens aux mathématiques
- Axiomatisation
- Décidabilité : il y a t il un programme qui détermine la terminaison d'autres programmes ?

#### I.1.3. Les trois formes de raisonnements

> Les mêmes causes produisent les mêmes effets

$$
A \to B
$$

- $A$ est la cause, l'hypothèse, la *prémisse*
- $B$ est la conséquence, la conclusion
- **Déduction** : à partir de la cause et de la règle, trouver les conséquences
- **Abduction** : à partir de la règle et des conséquences, trouver les causes
- **Induction** : à partir des causes et des conséquences, trouver la règle

Seule la déduction est **valide** : si les causes et les règles générales sont justes, les conséquences sont certaines.

*Mais aussi raisonnement par cas, raisonnement plausible, raisonnement par analogie, etc.*

###### Exemples :

Les Ferrari sont des voitures rouges.
$$
F \to R
$$
Les voitures qui ne sont pas rouges sont des Ferrari ?
$$
\mathrm{Non}(R) \to \mathrm{Non}(F)
$$
As-t-on :
$$
R \to F
$$

Argument fallacieux: l'ISF engendre l'évasion fiscale, donc il suffit de supprimer l'ISF pour supprimer l'évasion fiscale.

#### I.1.4. Applications

- Vérifications de circuits
- Preuves de programmes
- BDD déductive

#### I.1.5. La logique propositionnelle

## II. Le langage

- $V_{S} = \{ a, b, c, \dots, p,q, \dots \}$
- $V_{C} = \{ \wedge, \to, \leftrightarrow, \dots \}$ ensemble de connecteurs (reps. d'arité 1, 2, 2, 2, 2, 0, 0)

###### Remarque
Les connecteurs $\neg$ et $\vee$ forment un système complet

##### Définition (*formules propositionnelles bien formées*)

### II.2. Priorité des opérateur

$$
\neg > \wedge > \vee > \to; \leftrightarrow
$$
### II.3. Littéral

##### Définition (*littéral*)
C'est une variable propositionnelle ou sa négation.

### II.4. Représentation sous formes de graphes

Sous la forme d'un arbre binaire ordonné

- Chaque feuille de l'arbre correspondent à une variable propositionnelle
- Les autres correspondent à des connecteurs

###### Exemple
$$
\neg a \vee b \to c
$$

On peut représenter une formule sous forme de DAG (graphe dirigé acyclique) pour représenter une formule de façon plus concise/compacte...

###### Exemple
$$
a \vee b \to c \wedge (a \vee b)
$$

###### Note

## III. Sémantique

**Objectif :** donner des valeurs de vérité aux formules

Pour cela : deux valeurs vrai/faux (*tiers exclu*)
$$
\{ V, F \}
$$
### III.1. Interprétation

##### Définition (*Interprétation*)

Une *interprétation* $\omega$ est une application de $V_{S}$ dans $\{ V,S \}$ qui associe à chaque proposition la valeur $V$ ou $F$.

###### Remarque
- Tous les éléments dans l'ensemble de départ ont une valeur par l'application.
- Si $|V_{S}| = n$, alors il y a $2^{n}$ interprétations.

###### Note 

### III.2. Valuation

##### Définition (*valuation*)

Soit $\varphi$ une formule bien formée et $\omega \in \Omega$, la *valuation* de $\varphi$ pour $\omega$ ...

###### Remarque
- $A \to B$ équivaut à $\neg A \vee B$.
- On est sûr que la valuation se termine car à chaque étape un connecteur est résolu.

###### Note

##### Définition (*modèle et contre-modèle*)

- $\omega$ satisfait $\varphi$, noté XXX ssi $Val(\varphi), \omega = V$. On dit que $\omega$ est un *modèle* de $\varphi$.

##### Définition

Une formule propositionnelle $\varphi$ est dite :

- valide ...
- contradictoire
- satisfiable
- contigente

### III.3. Calculer la validité d'une formule