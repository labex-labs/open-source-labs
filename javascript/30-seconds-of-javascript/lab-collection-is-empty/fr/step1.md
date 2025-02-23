# Vérifier si une collection est vide

Pour vérifier si une collection est vide, vous pouvez ouvrir le Terminal/SSH et taper `node`. Ce programme vérifie si une valeur est un objet/collection vide, n'a pas de propriétés énumérables ou est de tout type qui n'est pas considéré comme une collection.

Pour utiliser le programme, vérifiez si la valeur fournie est `null` ou si sa `length` est égale à `0`. Voici un exemple de code :

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

Vous pouvez ensuite tester le programme à l'aide des codes suivants :

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - type n'est pas considéré comme une collection
isEmpty(true); // true - type n'est pas considéré comme une collection
```
