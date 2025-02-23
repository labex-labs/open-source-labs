# Algorithme des permutations de chaînes de caractères

Pour générer toutes les permutations d'une chaîne de caractères qui contient des doublons, utilisez l'algorithme suivant :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursion pour créer toutes les permutations possibles de la chaîne donnée.
3. Pour chaque lettre dans la chaîne donnée, créez toutes les permutations partielles pour le reste de ses lettres.
4. Utilisez `Array.prototype.map()` pour combiner la lettre avec chaque permutation partielle.
5. Utilisez `Array.prototype.reduce()` pour combiner toutes les permutations dans un tableau.
6. Les cas de base sont pour `String.prototype.length` égal à `2` ou `1`.
7. ⚠️ **AVERTISSEMENT** : Le temps d'exécution augmente exponentiellement avec chaque caractère. Pour des chaînes de plus de 8 à 10 caractères, l'environnement peut se bloquer car il essaie de résoudre toutes les combinaisons différentes.

Voici le code JavaScript pour l'algorithme :

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

Vous pouvez tester la fonction `stringPermutations` avec le code suivant :

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
