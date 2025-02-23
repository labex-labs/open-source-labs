# Comment retarder l'exécution d'une fonction en JavaScript

Pour retarder l'exécution d'une fonction en JavaScript, vous pouvez utiliser la méthode `setTimeout()`. Voici comment procéder :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la syntaxe suivante pour retarder l'exécution d'une fonction `fn` de `ms` millisecondes :

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. Pour passer des arguments à la fonction, utilisez l'opérateur de propagation (`...`) comme ceci :

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "plus tard"
); // Affiche 'plus tard' après une seconde.
```

Avec ce code, la fonction `fn` fournie sera appelée après le nombre spécifié de millisecondes (`ms`). Le paramètre `...args` vous permet de passer un nombre arbitraire d'arguments à la fonction.
