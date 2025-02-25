# Ordre de construction du graphe

## Problème

Étant donné une liste de projets et de leurs dépendances, nous devons trouver un ordre de construction valide. Un ordre de construction est une liste de projets dans laquelle chaque projet apparaît avant tout projet qui en dépend.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- L'entrée peut contenir un graphe cyclique.
- Nous pouvons supposer que nous disposons déjà des classes Graph et Node.
- Nous pouvons supposer que le graphe est connexe.
- Nous pouvons supposer que les entrées sont valides.
- Nous pouvons supposer que le problème rentre en mémoire.

## Exemple

Supposons que nous ayons les projets et dépendances suivants :

- projets : a, b, c, d, e, f, g
- dépendances : (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)

La sortie devrait être : d, f, c, b, g, a, e

Remarque : la direction de l'arête est vers le bas, ce qui signifie qu'un projet dépend des projets situés en dessous de lui.

```txt
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
```

Si l'entrée contient un graphe cyclique, la sortie devrait être None.
