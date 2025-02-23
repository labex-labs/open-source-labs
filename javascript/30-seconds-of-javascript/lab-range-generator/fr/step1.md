# Range Generator

Pour générer une plage de valeurs en utilisant un pas donné, utilisez la fonction `rangeGenerator` suivante. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.

- Utilisez une boucle `while` et `yield` pour renvoyer chaque valeur, en commençant par `start` et en terminant à `end`.
- Si vous voulez utiliser un pas par défaut de `1`, omettez le troisième argument.

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

Voici un exemple de manière d'utiliser la fonction `rangeGenerator` :

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// Affiche 6, 7, 8, 9
```
