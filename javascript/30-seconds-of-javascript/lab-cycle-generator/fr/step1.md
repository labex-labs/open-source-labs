# Instructions pour le générateur de cycle

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Ensuite, créez un générateur qui boucle indéfiniment sur le tableau donné. Voici les étapes :

1. Utilisez une boucle `while` non terminante qui `yield` une valeur chaque fois que `Generator.prototype.next()` est appelé.
2. Utilisez l'opérateur modulo (`%`) avec `Array.prototype.length` pour obtenir l'index de la prochaine valeur et incrémenter le compteur après chaque instruction `yield`.

Voici un exemple de la fonction `cycleGenerator` :

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

Vous pouvez ensuite utiliser la fonction comme suit :

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

Avec ces instructions, vous pouvez créer un générateur de cycle qui boucle indéfiniment sur n'importe quel tableau.
