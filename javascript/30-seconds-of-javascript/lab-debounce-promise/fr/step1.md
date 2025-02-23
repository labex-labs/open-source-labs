# Debounce Promise

Pour créer une fonction anti-basculement qui renvoie une promesse, en différant l'appel de la fonction fournie jusqu'à ce qu'au moins `ms` millisecondes se soient écoulées depuis la dernière fois qu'elle a été appelée, utilisez les étapes suivantes :

1. Chaque fois que la fonction anti-basculement est appelée, annulez le délai en attente actuel avec `clearTimeout()`, puis utilisez `setTimeout()` pour créer un nouveau délai qui différera l'appel de la fonction jusqu'à ce qu'au moins `ms` millisecondes se soient écoulées.
2. Utilisez `Function.prototype.apply()` pour appliquer le contexte `this` à la fonction et fournir les arguments nécessaires.
3. Créez une nouvelle `Promise` et ajoutez ses callbacks `resolve` et `reject` à la pile des promesses en attente.
4. Lorsque `setTimeout()` est appelé, copiez la pile actuelle (car elle peut changer entre l'appel de la fonction fournie et sa résolution), videz-la et appelez la fonction fournie.
5. Lorsque la fonction fournie se résout/rejette, résolvez/rejetez toutes les promesses de la pile (copiée lors de l'appel de la fonction) avec les données renvoyées.
6. Omettez le second argument, `ms`, pour définir le délai à la valeur par défaut de `0` ms.

Voici le code pour la fonction `debouncePromise()` :

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

Voici un exemple d'utilisation de `debouncePromise()` :

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// Affichera ['resolved', 'bar'] les deux fois
```
