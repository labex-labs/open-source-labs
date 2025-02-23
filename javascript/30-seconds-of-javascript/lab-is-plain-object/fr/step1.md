# Vérifiez si une valeur est un objet simple

Pour vérifier si une valeur est un objet simple, suivez ces étapes :

- Vérifiez si la valeur est véridique.
- Utilisez `typeof` pour vérifier si c'est un objet.
- Utilisez `Object.prototype.constructor` pour vous assurer que le constructeur est égal à `Object`.

Utilisez le code suivant pour implémenter cette vérification :

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

Vous pouvez tester cette fonction avec les exemples suivants :

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
