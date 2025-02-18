# Vérification du zéro négatif

Pour vérifier si un nombre est un zéro négatif, ouvrez le Terminal/SSH et entrez `node`. Ensuite, utilisez le code suivant :

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

Cela vérifiera si la valeur passée est égale à `0` et si `1` divisé par cette valeur est égal à `-Infinity`. Par exemple :

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
