# Conversion d'une fonction en fonction variadique

Pour convertir une fonction qui accepte un tableau en une fonction variadique, vous pouvez suivre les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Retournez une fermeture qui collecte toutes les entrées dans une fonction acceptant un tableau.

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. Utilisez la fonction `collectInto` pour convertir une fonction en une fonction variadique.

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (après environ 2 secondes)
```

Cela vous permettra d'accepter un nombre quelconque d'arguments dans votre fonction et de les collecter dans un tableau pour un traitement ultérieur.
