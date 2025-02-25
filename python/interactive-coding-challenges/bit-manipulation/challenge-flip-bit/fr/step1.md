# Basculer un bit

## Problème

Étant donné un nombre binaire, nous devons basculer l'un de ses bits de 0 à 1 pour maximiser la plus longue séquence de 1. Par exemple, si nous avons le nombre binaire `000011110000`, nous pouvons basculer le quatrième bit de 0 à 1 pour obtenir `000111110000`, qui a une séquence de cinq 1. Notre objectif est d'écrire une fonction Python qui prend un nombre binaire en entrée et renvoie la longueur de la plus longue séquence de 1 après avoir basculé un bit.

## Exigences

Les exigences pour notre fonction Python sont les suivantes :

- L'entrée doit être un entier en base 2.
- Nous pouvons supposer que l'entrée est un nombre sur 32 bits.
- Nous n'avons pas besoin de valider la longueur de l'entrée.
- La sortie doit être un entier.
- Nous ne pouvons pas supposer que les entrées sont valides.
- Nous pouvons supposer que nous utilisons un nombre positif puisque Python n'a pas d'opérateur >>>.
- Nous pouvons supposer que cela tient en mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu de notre fonction Python :

- `None` -> Exception
- `11111111111111111111111111111111` -> 32
- `00000000000000000000000000000000` -> 1
- `00001111110111011111001111110000` -> 10
