# Vérifier si une valeur est un objet

Pour vérifier si une valeur passée est un objet, ouvrez le Terminal/SSH et tapez `node`. Les étapes suivantes sont effectuées :

- Le constructeur `Object` crée un wrapper d'objet pour la valeur donnée.
- Si la valeur est `null` ou `undefined`, un objet vide est créé et renvoyé.
- Si la valeur n'est pas `null` ou `undefined`, un objet d'un type correspondant à la valeur donnée est renvoyé.

Voici une fonction d'exemple qui vérifie si une valeur est un objet :

```js
const isObject = (obj) => obj === Object(obj);
```

Voici quelques exemples d'utilisation de la fonction `isObject` :

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
