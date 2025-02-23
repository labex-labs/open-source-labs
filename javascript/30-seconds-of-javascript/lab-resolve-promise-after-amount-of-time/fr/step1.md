# Création d'une promesse avec un délai

Pour créer une nouvelle promesse qui est résolue après un délai spécifique, suivez ces étapes :

1. Utilisez le constructeur `Promise` pour créer une nouvelle promesse.
2. Dans la fonction exécutrice de la promesse, utilisez `setTimeout()` pour appeler la fonction `resolve` de la promesse avec la `value` fournie après le `delay` spécifié.

Voici une implémentation exemple de `resolveAfter()` :

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

Maintenant, vous pouvez appeler `resolveAfter()` pour obtenir une promesse qui est résolue avec la valeur fournie après le délai spécifié :

```js
resolveAfter("Hello", 1000);
// Retourne une promesse qui est résolue avec 'Hello' après 1s
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal ou SSH et tapez `node`.
