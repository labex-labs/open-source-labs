# Vérifier si une valeur est une fonction

Pour vérifier si une valeur est une fonction, vous pouvez utiliser l'opérateur `typeof` avec le type primitif `function`.

Voici un exemple d'une fonction qui vérifie si une valeur donnée est une fonction :

```js
const isFunction = (val) => typeof val === "function";
```

Vous pouvez l'utiliser comme ceci :

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
