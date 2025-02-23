# Promesses JavaScript

Pour vérifier si un objet est similaire à une Promesse, utilisez la fonction `isPromiseLike`. Cette fonction vérifie si l'objet n'est pas nul, a un type d'objet ou de fonction et a une propriété `.then` qui est également une fonction.

Voici le code pour `isPromiseLike` :

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

Voici quelques exemples d'utilisation de `isPromiseLike` :

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

Pour commencer à pratiquer la programmation en JavaScript, ouvrez le Terminal/SSH et tapez `node`.
