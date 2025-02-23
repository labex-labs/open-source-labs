# Fonction pour obtenir le type d'une valeur

Pour obtenir le type d'une valeur, utilisez la fonction suivante :

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- La fonction renvoie `'undefined'` ou `'null'` si la valeur est `undefined` ou `null`.
- Sinon, elle renvoie le nom du constructeur en utilisant `Object.prototype.constructor` et `Function.prototype.name`.

Utilisation exemple :

```js
getType(new Set([1, 2, 3])); // 'Set'
```
