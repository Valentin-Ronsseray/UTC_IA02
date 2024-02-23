#Cours #IA02 #P24
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
		- [[#II.1. Variables propositionnelles et correcteurs|II.1. Variables propositionnelles et correcteurs]]
					- [[#Remarque|Remarque]]
				- [[#Définition (*formules propositionnelles bien formées*)|Définition (*formules propositionnelles bien formées*)]]
		- [[#II.2. Priorité des opérateur|II.2. Priorité des opérateur]]
		- [[#II.3. Littéral|II.3. Littéral]]
				- [[#Définition (*littéral*)|Définition (*littéral*)]]
		- [[#II.4. Représentation sous formes de graphes|II.4. Représentation sous formes de graphes]]
					- [[#Exemple|Exemple]]
					- [[#Note manuscrite|Note manuscrite]]
	- [[#III. Sémantique|III. Sémantique]]
		- [[#III.1. Interprétation|III.1. Interprétation]]
				- [[#Définition (*Interprétation*)|Définition (*Interprétation*)]]
					- [[#Remarque|Remarque]]
					- [[#Note manuscrite|Note manuscrite]]
		- [[#III.2. Valuation|III.2. Valuation]]
				- [[#Définition (*valuation*)|Définition (*valuation*)]]
					- [[#Remarque|Remarque]]
					- [[#Note manuscrite|Note manuscrite]]
				- [[#Définition (*modèle et contre-modèle*)|Définition (*modèle et contre-modèle*)]]
				- [[#Définition|Définition]]
		- [[#III.3. Calculer la validité d'une formule|III.3. Calculer la validité d'une formule]]

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

### II.1. Variables propositionnelles et correcteurs

- $V_{S} = \{ a, b, c, \dots, p,q, \dots \}$
- $V_{C} = \{\neg,  \wedge, \vee \to, \leftrightarrow, \bot, \top \}$

###### Remarque
- Les connecteurs $\neg$ et $\vee$ forment un système complet
- 
  > [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=10&selection=9,9,9,15&color=yellow|IA02 _ Logique Propositionnelle, page 10]]
> > arité 
> 
> L'*arité* d'un connecteur correspond au nombre d'arguments que l'on peut associer au connecteur.

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
> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=13&selection=20,0,29,1&color=yellow|IA02 _ Logique Propositionnelle, page 13]]
> > $\neg a \vee b \to c$
> 
> 
![[diagram-20240221.svg#invert_B]]


> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=13&selection=12,0,16,17|IA02 _ Logique Propositionnelle, page 13]]
> > $a \vee b \to c \wedge (a \vee b)$
> > On peut représenter une formule sous forme de DAG (graphe dirigé acyclique) pour représenter une formule de façon plus concise/compacte…
> 
> ![[diagram-20240223.svg#invert_B]]

###### Note manuscrite

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

###### Note manuscrite

### III.2. Valuation

##### Définition (*valuation*)

Soit $\varphi$ une formule bien formée et $\omega \in \Omega$, la *valuation* de $\varphi$ pour $\omega$... 

###### Remarque
- $A \to B$ équivaut à $\neg A \vee B$.
- On est sûr que la valuation se termine car à chaque étape un connecteur est résolu.

###### Note manuscrite

##### Définition (*modèle et contre-modèle*)

Soit $\varphi$ une formule bien formée et $\omega\in\Omega$, la valuation de $\varphi$ pour $\omega$ (notée $Val(\varphi,\omega))$ est telle que :
- si $\varphi$ est une variable propositionnelle, alors $Val(\varphi,\omega)=\omega(\varphi)$ ;
- $Val(\top,\omega)=V$ et $Val(\bot,\omega)=F;$
- si $\varphi$ est de la forme $\lnot A$ (resp. $A\land B,A\lor B,A\rightarrow B,A\leftrightarrow B)$, alors appliquer récursivement la table de vérité suivante.

| **$A$** | **$B$** | **$\neg A$** | **$A \wedge B$** | **$A \vee B$** | **$A \to B$** | **$A\leftrightarrow B$** |
| ------- | ------- | ------------ | ---------------- | -------------- | ------------- | ------------------------ |
| $F$     | $F$     | $V$          | $F$              | $F$            | $V$           | $V$                      |
| $F$     | $V$     | $V$          | $F$              | $V$            | $V$           | $F$                      |
| $V$     | $F$     | $F$          | $F$              | $V$            | $F$           | $F$                      |
| $V$     | $V$     | $F$          | $V$              | $V$            | $V$           | $V$                      |

##### Définition
Une formule propositionnelle $\varphi$ est dite :
- *valide* (noté $\models\varphi$ ) ssi pour toute interprétation $\omega\in\Omega$ on a $\omega\models\varphi$. Dans ce cas $\varphi$ est également appelé *tautologie* ;
- *contradictoire* ssi pour toute interprétation $\omega\in\Omega$ on a $\omega\nvDash\varphi$ ; 
- *satisfiable* ssi elle n'est pas contradictoire ;
- *contingente* ssi il existe $\omega\in\Omega$ tel que $\omega\models\varphi$ et il existe $\omega^{\prime}\in\Omega$ tel que $\omega^{\prime}\not\models\varphi.$


### III.3. Calculer la validité d'une formule

