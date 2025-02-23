# Vérifiez si une valeur est semblable à un tableau

Pour vérifier si une valeur est semblable à un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node`.
3. Utilisez le code suivant pour vérifier si l'argument fourni est itérable :

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. La fonction renverra `true` si l'argument fourni est un objet semblable à un tableau, et `false` sinon.
5. Par exemple :

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
