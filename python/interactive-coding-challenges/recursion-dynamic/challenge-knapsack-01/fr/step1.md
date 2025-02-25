# Sac à dos 0/1

## Problème

Étant donné un sac à dos avec une capacité totale de poids et une liste d'objets ayant un poids w(i) et une valeur v(i), déterminer quels objets sélectionner pour maximiser la valeur totale. Le problème est connu sous le nom de problème du sac à dos 0/1 car chaque objet ne peut être sélectionné qu'une seule fois (début 0/1). Le problème est NP-difficile, ce qui signifie qu'il n'existe pas d'algorithme en temps polynomial connu qui puisse le résoudre de manière optimale pour tous les cas.

## Exigences

Pour résoudre le problème du sac à dos, nous devons prendre en compte les exigences suivantes :

- Les objets ne peuvent pas être remplacés une fois qu'ils sont placés dans le sac à dos.
- Nous ne pouvons pas diviser un objet.
- Nous ne pouvons pas avoir un objet d'entrée avec un poids ou une valeur de 0.
- Nous ne pouvons pas supposer que les entrées sont valides.
- Les entrées devraient être triées par rapport à la valeur/poids.
- Nous pouvons supposer que le problème rentre en mémoire.

## Exemple

Voici un exemple de l'utilisation de l'algorithme du sac à dos :

```txt
poids total = 8
objets
  v | w
  0 | 0
a 2 | 2
b 4 | 2
c 6 | 4
d 9 | 5

valeur maximale = 13
objets
  v | w
b 4 | 2
d 9 | 5
```

Dans cet exemple, nous avons un sac à dos avec une capacité totale de poids de 8 et quatre objets avec leurs valeurs et poids respectifs. Nous devons sélectionner les objets qui maximisent la valeur totale tout en gardant le poids dans la capacité du sac à dos. La solution optimale est de sélectionner les objets b et d, qui ont une valeur totale de 13 et un poids total de 7.
