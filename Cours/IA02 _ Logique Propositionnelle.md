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
	- [[#III. Sémantique|III. Sémantique]]
		- [[#III.1. Interprétation|III.1. Interprétation]]
				- [[#Définition (*Interprétation*)|Définition (*Interprétation*)]]
					- [[#Remarque|Remarque]]
		- [[#III.2. Valuation|III.2. Valuation]]
				- [[#Définition (*valuation*)|Définition (*valuation*)]]
					- [[#Remarque|Remarque]]
				- [[#Définition (*modèle et contre-modèle*)|Définition (*modèle et contre-modèle*)]]
				- [[#Définition|Définition]]
					- [[#Exemple|Exemple]]
		- [[#III.3. Calculer la validité d'une formule|III.3. Calculer la validité d'une formule]]
			- [[#III.3.1. Algorithme de Quine|III.3.1. Algorithme de Quine]]
			- [[#III.3.2. Absurde|III.3.2. Absurde]]
		- [[#III.4. Conséquence logique|III.4. Conséquence logique]]
					- [[#Exemple|Exemple]]
		- [[#III.5. Théorèmes|III.5. Théorèmes]]
		- [[#III.6. Wumpus|III.6. Wumpus]]
					- [[#Avertissement|Avertissement]]
	- [[#IV. Clauses et calcul propositionnel|IV. Clauses et calcul propositionnel]]

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

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=10&selection=45,0,57,19&color=yellow|IA02 _ Logique Propositionnelle, page 10]]
> > Si et sont des formules alors , , et sont des formules ;
> 
> Les parenthèses sont très importantes
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
> ![[diagram-20240221.svg#invert_B]]

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=13&selection=12,0,16,17|IA02 _ Logique Propositionnelle, page 13]]
> > $a \vee b \to c \wedge (a \vee b)$
> > On peut représenter une formule sous forme de DAG (graphe dirigé acyclique) pour représenter une formule de façon plus concise/compacte…
> 
> ![[diagram-20240223.svg#invert_B]]

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
![[InsertionObsidian_annoté.png]]

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=15&selection=52,0,52,1&color=yellow|IA02 _ Logique Propositionnelle, page 15]]
> > Ω
> 
> $\Omega = \{ V,F \}^{V_{s}}$

### III.2. Valuation

##### Définition (*valuation*)

Soit $\varphi$ une formule bien formée et $\omega\in\Omega$, la *valuation* de $\varphi$ pour $\omega$ (notée $Val(\varphi,\omega))$ est telle que :
- si $\varphi$ est une variable propositionnelle, alors $Val(\varphi,\omega)=\omega(\varphi)$ ;
- $Val(\top,\omega)=V$ et $Val(\bot,\omega)=F;$
- si $\varphi$ est de la forme $\lnot A$ (resp. $A\land B,A\lor B,A\rightarrow B,A\leftrightarrow B)$, alors appliquer récursivement la table de vérité suivante.

| **$A$** | **$B$** | **$\neg A$** | **$A \wedge B$** | **$A \vee B$** | **$A \to B$** | **$A\leftrightarrow B$** |
| ------- | ------- | ------------ | ---------------- | -------------- | ------------- | ------------------------ |
| $F$     | $F$     | $V$          | $F$              | $F$            | $V$           | $V$                      |
| $F$     | $V$     | $V$          | $F$              | $V$            | $V$           | $F$                      |
| $V$     | $F$     | $F$          | $F$              | $V$            | $F$           | $F$                      |
| $V$     | $V$     | $F$          | $V$              | $V$            | $V$           | $V$                      |

###### Remarque
- $A \to B$ équivaut à $\neg A \vee B$.
- On est sûr que la valuation se termine car à chaque étape un connecteur est résolu.

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=17&selection=4,0,13,1&color=yellow|IA02 _ Logique Propositionnelle, page 17]]
> > ω = {a, b, ¬c}
> 
> $$ \begin{cases} \omega(a) = \omega(b) = V  \\ \omega(c) = F \end{cases}$$

##### Définition (*modèle et contre-modèle*)
- $\omega$ satisfait $\varphi$,noté $\omega\models\varphi$ ssi $Val(\varphi,\omega)=V$. On dit alors que $\omega$ est un modèle de $\varphi.$
- L'ensemble des modèles de $\varphi$ est noté $Mod(\varphi)$ :
$$
Mod(\varphi)=\{\omega\in\Omega:\omega\models\varphi\}
$$
- $\omega$ falsifie $\varphi$, noté $\omega\nvDash\varphi$ ssi $Val(\varphi,\omega)=F$. On dit alors que $\omega$ est un contremodèle de $\varphi.$

##### Définition
Une formule propositionnelle $\varphi$ est dite :
- *valide* (noté $\models\varphi$ ) ssi pour toute interprétation $\omega\in\Omega$ on a $\omega\models\varphi$. Dans ce cas $\varphi$ est également appelé *tautologie* ;
- *contradictoire* ssi pour toute interprétation $\omega\in\Omega$ on a $\omega\nvDash\varphi$ ; 
- *satisfiable* ssi elle n'est pas contradictoire ;
- *contingente* ssi il existe $\omega\in\Omega$ tel que $\omega\models\varphi$ et il existe $\omega^{\prime}\in\Omega$ tel que $\omega^{\prime}\not\models\varphi.$

###### Exemple
Les formules suivantes sont des tautologies
- $p \to p$
- $p \vee \neg p$
- $\neg (\neg p \wedge p)$
- $p \wedge q \to q$

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=19&selection=32,0,36,33|IA02 _ Logique Propositionnelle, page 19]]
> > satisable ssi elle n'est pas contradictoire
> 
> ssi $\exists \omega \in \Omega, \omega \models \varphi$

### III.3. Calculer la validité d'une formule

#### III.3.1. Algorithme de Quine
> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=20&selection=22,0,22,16&color=yellow|IA02 _ Logique Propositionnelle, page 20]]
> > (règle de Morgan
> 
> ![[InsertionObsidian_annoté 2.png]]

#### III.3.2. Absurde

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=20&selection=53,0,54,1&color=yellow|IA02 _ Logique Propositionnelle, page 20]]
> > φ2
> 
> ![[InsertionObsidian_annoté 3.png]]

### III.4. Conséquence logique

###### Exemple


> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=22&selection=45,0,53,1|IA02 _ Logique Propositionnelle, page 22]]
> > a ⊨ a ∨ b
> 
> $\text{Mod}(a) =\{ \{ a,b \} \}, \{ a,\neg b \} \}$ et $\text{Mod}(a \vee b) = \{ \{ a,b \}, \{ a, \neg b \}, \{ \neg a, b \} \}$.

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=22&selection=55,0,66,1|IA02 _ Logique Propositionnelle, page 22]]
> > a, a → b ⊨ b
> 
> $\text{Mod}(a) = \{ \{ a, b \}, \{ a, \neg b \} \}$, $\text{Mod}(a \to b) = \{ \{ a,b \}, \{ \neg a, \neg b \}, \{ \neg a, b \} \}$ et $\text{Mod}(b) = \{ \{ a,b \}, \{ \neg a,b \} \}$

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=22&selection=68,0,78,1|IA02 _ Logique Propositionnelle, page 22]]
> > ⊥⊨ a → b ∨ c
> 
> $$ \text{Mod}(\bot) = \emptyset \subset \text{Mod}(a \to b \vee c)$$

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=22&selection=2,0,3,0|IA02 _ Logique Propositionnelle, page 22]]
> > Par extension :
>
> $$\bigcap_{i=1}^{n} \text{Mod}(\varphi_{i}) \subset \text{Mod}(\psi) $$

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=23&selection=4,0,4,19|IA02 _ Logique Propositionnelle, page 23]]
> > Équivalence logique
> 
> $$\varphi_{1} \equiv \varphi_{2} \iff \text{Mod}(\varphi_{1}) = \text{Mod}(\varphi_{2}) $$

> [!PDF] [[IA02 _ Logique Propositionnelle.pdf#page=23&selection=24,0,30,12&color=yellow|IA02 _ Logique Propositionnelle, page 23]]
> > Avant de chercher à déduire quoi que se soit d'un ensemble de formules, il faut toujours vérier préalablement leur cohérence (c.-à-d. prouver l'existence d'au moins un modèle) !
> 
> C'est comme une récurrence : il faut l'initialisation !

### III.5. Théorèmes

> [!PDF|] [[IA02 _ Logique Propositionnelle.pdf#page=24&selection=4,0,4,25|IA02 _ Logique Propositionnelle, page 24]]
> > Théorème de la déduction 
>  
> ###### Démonstration
$\implies$) Supposons que
> $$
> \varphi_{1}, \dots, \varphi_{n} \models \psi
> $$
> Alors
> $$
> \bigcap_{i=1}^{n} \mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\psi)
> $$
> D'où
> $$
> \left( \bigcap_{i=1}^{n} \mathrm{Mod}(\varphi_{i}) \right) \cup \mathrm{Mod}(\varphi_{n})^{C}\subset \mathrm{Mod}(\psi) \cup \mathrm{Mod}(\varphi_{n})^{C}
> $$
> Ainsi par distributivité de $\cup$ sur $\cap$,
> $$
> \left( \bigcap_{i=1}^{n-1} \mathrm{Mod}(\varphi_{i}) \right) \cup \mathrm{Mod}(\varphi_{n})^{C}\subset \mathrm{Mod}(\psi) \cup \mathrm{Mod}(\varphi_{n})^{C}
> $$
> D'une part
> $$
> \bigcap_{i=1}^{n-1} \mathrm{Mod}(\varphi_{i}) \subset \left( \bigcap_{i=1}^{n-1} \mathrm{Mod}(\varphi_{i}) \right) \cup \mathrm{Mod}(\varphi_{n})^{C}
> $$
> D'autre part, on observe que
> $$
> \mathrm{Mod}(\psi) \cup \mathrm{Mod}(\varphi_{n})^{C} = \mathrm{Mod}(\varphi_{n} \to \psi)
> $$
> (il s'agit bien du complémentaire de $\mathrm{Mod}(\varphi_{n}) \cap \mathrm{Mod}(\psi)^{C}$.)
> 
> Par conséquent
> $$
> \bigcap_{i=1}^{n-1}\mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\varphi_{n} \to \psi)
> $$
> 
> i.e
> $$
> \varphi_{1},\dots,\varphi_{n-1} \models \varphi_{n} \to \psi
> $$
> 
> $\Longleftarrow$ ) Supposons que
> $$
> \varphi_{1},\dots,\varphi_{n-1} \models \varphi_{n} \to \psi
> $$
> Alors
> $$
> \bigcap_{i=1}^{n-1}\mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\varphi_{n} \to \psi)
> $$
> que l'on peut écrire
> $$
> \bigcap_{i=1}^{n-1}\mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\psi) \cup \mathrm{Mod}(\varphi_{n})^{C}
> $$
> On a alors
> $$
> \left( \bigcap_{i=1}^{n-1}\mathrm{Mod}(\varphi_{i}) \right) \cap \mathrm{Mod}(\varphi_{n}) \subset (\mathrm{Mod}(\psi) \cup \mathrm{Mod}(\varphi_{n})^{C}) \cap \mathrm{Mod}(\varphi_{n})
> $$
> D'où par distribution de $\cap$ sur $\cup$ et réécriture
> $$
> \bigcap_{i=1}^{n}\mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\psi ) \cap \mathrm{Mod}(\varphi_{n})
> $$
> Or on a déjà $\displaystyle \bigcap_{i=1}^{n}\mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\varphi_{n})$, et donc
> $$
> \bigcap_{i=1}^{n}\mathrm{Mod}(\varphi_{i}) \subset \mathrm{Mod}(\psi )
> $$
> C'est-à-dire
> $$
> \varphi_{1}, \dots, \varphi_{n} \models \psi
> $$

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=24&selection=6,0,6,14&color=yellow|IA02 _ Logique Propositionnelle, page 24]]
> > Corollaire 1 :
> 
> Prendre $\varphi_{1}, \dots, \varphi_{n-1} = \top$ et $\varphi_{n} = \varphi$.

> [!PDF] [[IA02 _ Logique Propositionnelle.pdf#page=25&selection=8,0,8,12&color=yellow|IA02 _ Logique Propositionnelle, page 25]]
> > Corollaire 3
> 
> Raisonnement par l'absurde

### III.6. Wumpus

###### Avertissement
**Utiliser l'implication en priorité sur les équivalences pour les représentations logiques**

## IV. Clauses et calcul propositionnel

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=39&selection=7,0,12,32&color=yellow|IA02 _ Logique Propositionnelle, page 39]]
> >  un cube est une conjonction de littéraux
> 
> ##### Définition (*Pureté d'un cube*)
> On dit qu'un cube est *pur* ssi chaque variable n'apparaît qu'une fois.

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=41&selection=28,0,39,1&color=yellow|IA02 _ Logique Propositionnelle, page 41]]
> > ¬a ∨ b a → b
> 
> On applique Morgan sur $\neg (a \wedge \neg b)$

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=41&selection=128,0,138,0&color=yellow|IA02 _ Logique Propositionnelle, page 41]]
> > a, b → c, 
> 
> A gauche de la flèche, disjonction; à droite, conjonction.

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=44&selection=4,0,4,32&color=yellow|IA02 _ Logique Propositionnelle, page 44]]
> > Mettre sous forme CNF la formule
> 
> ![[InsertionObsidian_annoté 4.png]]

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=46&selection=29,0,39,3&color=yellow|IA02 _ Logique Propositionnelle, page 46]]
> > R2 B1,1 P1,2 P2,1
> 
> ![[InsertionObsidian_annoté 5.png]]

> [!PDF|red] [[IA02 _ Logique Propositionnelle.pdf#page=47&selection=30,0,30,45&color=red|IA02 _ Logique Propositionnelle, page 47]]
> > Ou encore sous forme de règle de réécriture :
> 
> $B$ doit être un **littéral** !

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=47&selection=2,0,2,22&color=yellow|IA02 _ Logique Propositionnelle, page 47]]
> > Principe de résolution
> 
> On peut retrouver le *modus ponens* en introduisant une contradiction

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=48&selection=11,0,11,21&color=yellow|IA02 _ Logique Propositionnelle, page 48]]
> > Version ensembliste :
> 
> On effectue des *modus ponens* successifs.

> [!PDF|note] [[IA02 _ Logique Propositionnelle.pdf#page=49&selection=26,0,26,1&color=note|IA02 _ Logique Propositionnelle, page 49]]
> > 4
> 
> Erreur de définition ?

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=49&selection=2,0,2,46&color=yellow|IA02 _ Logique Propositionnelle, page 49]]
> > Procédure automatique : Davis et Putnam (1960)
> 
> ###### Exemple
> ![[InsertionObsidian_annoté 6.png]]

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=57&selection=22,0,22,10&color=yellow|IA02 _ Logique Propositionnelle, page 57]]
> > Exercice :
> 
> ![[InsertionObsidian_annoté 7.png]]

> [!PDF|red] [[IA02 _ Logique Propositionnelle.pdf#page=62&selection=4,1,4,31&color=red|IA02 _ Logique Propositionnelle, page 62]]
> > rouver une conséquence logique
> 
> Le $\cup$ est une opération ensembliste et non logique ! ($\cup \not \equiv \vee$) On ajoute une clause à notre FNC.

> [!PDF|yellow] [[IA02 _ Logique Propositionnelle.pdf#page=69&selection=6,0,6,61&color=yellow|IA02 _ Logique Propositionnelle, page 69]]
> > Chaque sommet ne peut être colorié qu'avec une seule couleur 
> 
> $\neg S1R \to \neg S1G \wedge \neg S1B \equiv S1R \vee S1G \vee S1B$

