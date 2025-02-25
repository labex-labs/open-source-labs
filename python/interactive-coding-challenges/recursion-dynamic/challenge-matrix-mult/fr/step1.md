# Multiplication de matrices

## Problème

Étant donné une liste de matrices 2x2, nous devons trouver le coût minimal de leur multiplication. Le coût de la multiplication de deux matrices est le nombre de multiplications scalaires nécessaires. Par exemple, si nous avons les matrices A, B et C, et que nous voulons calculer le produit ABC, le coût serait le nombre de multiplications scalaires nécessaires pour calculer chaque élément de la matrice résultante.

Pour résoudre ce problème, nous devons trouver l'ordre optimal de multiplication des matrices. L'ordre dans lequel nous multiplions les matrices affecte le coût total de la multiplication. Par exemple, si nous avons les matrices A, B et C, et que nous voulons calculer le produit ABC, nous pouvons soit calculer (AB)C soit A(BC). Le coût de ces deux calculs peut être différent, et nous devons trouver l'ordre optimal qui minimise le coût.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- Nous n'avons besoin que de calculer le coût de la multiplication de matrices et non de lister l'ordre réel des opérations.
- Nous ne pouvons pas supposer que les entrées sont valides et devons gérer les entrées invalides.
- Nous pouvons supposer que le problème rentre en mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu de la fonction :

- `None` -> `Exception`
- `[]` -> `0`
- `[Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)]` -> `124`
