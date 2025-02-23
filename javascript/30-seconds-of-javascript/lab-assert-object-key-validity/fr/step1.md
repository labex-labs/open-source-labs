# Valider les clés d'un objet

Pour s'assurer que toutes les clés d'un objet correspondent aux `keys` spécifiées, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `Object.keys()` pour récupérer les clés de l'objet, `obj`.
- Utilisez `Array.prototype.every()` et `Array.prototype.includes()` pour valider que chaque clé de l'objet est incluse dans le tableau `keys`.

Voici une implémentation d'exemple :

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

Vous pouvez utiliser la fonction de cette manière :

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
