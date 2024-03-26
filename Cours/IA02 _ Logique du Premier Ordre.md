# Logique du Premier Ordre ^toc

- [[#Logique du Premier Ordre ^toc|Logique du Premier Ordre]]
	- [[#I. Introduction|I. Introduction]]
	- [[#II. Le language|II. Le language]]
		- [[#II.1. Les briques de base|II.1. Les briques de base]]
	- [[#III. Théorie des modèles|III. Théorie des modèles]]

## I. Introduction

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=4&selection=24,0,25,1&color=yellow|IA02 _ Logique du Premier Ordre, page 4]]
> > ∀x
> 
> Peut représenter n'importe quoi, même ta grand-mère.

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=4&selection=6,0,11,6&color=yellow|IA02 _ Logique du Premier Ordre, page 4]]
> > Rq: l'implication est utilisée comme ltrage
> 
> L'assertion mathématique $\forall x \in \mathrm{Pairs}, \quad x \% 2 = 0$ s'écrit en logique du premier ordre $\forall x \quad \mathrm{Pairs}(x) \to (x \% 2 = 0)$.

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=5&selection=25,0,36,1&color=yellow|IA02 _ Logique du Premier Ordre, page 5]]
> > ∀x∃y aime(x, y)
> 
> Avec les parenthèses : $(\forall x (\exists y \quad aime(x,y)))$.

## II. Le language

### II.1. Les briques de base

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=8&selection=40,0,40,62&color=yellow|IA02 _ Logique du Premier Ordre, page 8]]
> > les constantes peuvent être vues comme des fonctions d'arité 0
> 
> On a alors $C \subset F$.

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=11&selection=55,0,55,7&color=yellow|IA02 _ Logique du Premier Ordre, page 11]]
> > Exemple
> 
> ![[InsertionObsidian_annoté 8.png]]
> 
> ###### Remarque
> $q$ est un prédicat d'arité 0 : c'est une constante

> [!PDF|note] [[IA02 _ Logique du Premier Ordre.pdf#page=13&selection=35,0,52,2&color=note|IA02 _ Logique du Premier Ordre, page 13]]
> > p(x, y) ∨ (∀x q(x) ∧ r(x))
> 
> ###### Remarque
> On peut renommer le premier $x$ en $z$ parce que ce ne sont pas les mêmes variables malgré qu'elles aient la même écriture
> $$ p(z, y) ∨ (∀x \, q(x) ∧ r(x)) $$

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=15&selection=71,0,81,3&color=yellow|IA02 _ Logique du Premier Ordre, page 15]]
> > (x + 1) = x^2 + 2x + 1
> 
> $\forall x \quad( \mathrm{nombre}(x) \to ((x+1)^{2} = x^{2} + 2x +1))$

## III. Théorie des modèles

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=19&selection=8,0,8,38&color=yellow|IA02 _ Logique du Premier Ordre, page 19]]
> > B : Certains étudiants ont une voiture
> 
> $\Big(\exists x \quad \text{étudiant}(x) \wedge \big(\text{voiture}(y) \wedge \text{possède}(x,y)\big)\Big)$

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=19&selection=10,0,10,43&color=yellow|IA02 _ Logique du Premier Ordre, page 19]]
> > C : Certains étudiants n’ont pas de voiture
> 
> $\Big(\forall x \quad \text{étudiant} \wedge \big(\forall y \quad \text{voiture}(y) \to \neg \text{possède}(x,y)\big)\Big)$
> ce qui équivaut à
> $\Big(\exists x \quad \text{étudiant}(x) \wedge \neg\big(\exists y \quad \text{voiture}(y) \wedge \text{possède}(x,y)\big)\Big)$

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=19&selection=6,0,6,54&color=yellow|IA02 _ Logique du Premier Ordre, page 19]]
> > A : Toutes les voitures ont exactement un propriétaire
> 
> $\Big(\forall x \quad \text{voiture}(x) \to \big(\exists y \quad \text{possède}(y,x) \wedge \neg (\exists z \quad \text{possède}(z,x) \to \neg(z=y))\big)\Big)$

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=19&selection=54,0,61,1&color=yellow|IA02 _ Logique du Premier Ordre, page 19]]
> > D = {a, b}
> 
> $a$ est une voiture et $b$ est un étudiant

> [!PDF|yellow] [[IA02 _ Logique du Premier Ordre.pdf#page=38&selection=0,7,25,2&color=yellow|IA02 _ Logique du Premier Ordre, page 38]]
> >  ((∀x p(x)) ∧ (∃y q(y))) → (∃y p(y) ∧ q(y))
> 
> ![[InsertionObsidian_annoté 9.png]]

