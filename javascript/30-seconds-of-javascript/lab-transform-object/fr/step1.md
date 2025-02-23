# Transformation d'objet

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

La fonction `transform` applique une fonction spécifiée à un accumulateur et à chaque clé de l'objet, de gauche à droite. Voici comment l'utiliser :

- Utilisez `Object.keys()` pour itérer sur chaque clé de l'objet.
- Utilisez `Array.prototype.reduce()` pour appliquer la fonction spécifiée à l'accumulateur donné.

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

Voici un exemple :

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
