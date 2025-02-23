# Comment joindre un tableau en une chaîne de caractères

Pour joindre tous les éléments d'un tableau en une chaîne de caractères, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `join()` avec les paramètres suivants :
   - `arr` : le tableau à joindre.
   - `separator` (optionnel) : le séparateur à utiliser entre les éléments du tableau. Si non spécifié, le séparateur par défaut `,` sera utilisé.
   - `end` (optionnel) : le séparateur à utiliser entre les deux derniers éléments du tableau. Si non spécifié, la même valeur que `separator` sera utilisée par défaut.
3. La fonction `join()` utilise `Array.prototype.reduce()` pour combiner les éléments du tableau en une chaîne de caractères.
4. La chaîne de caractères finale est renvoyée.

Voici le code de la fonction `join()` :

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

Voici quelques exemples d'utilisation de la fonction `join()` :

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
