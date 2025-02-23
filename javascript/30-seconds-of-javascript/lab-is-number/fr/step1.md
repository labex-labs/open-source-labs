# Vérifier si une valeur est un nombre en JavaScript

Pour vérifier si une valeur est un nombre en JavaScript, vous pouvez utiliser l'opérateur `typeof` pour déterminer si la valeur est classée comme un nombre primitif. Pour éviter les problèmes avec `NaN`, qui a un `typeof` égal à `number` et n'est pas égal à lui-même, vous pouvez également vérifier si la valeur est égale à elle-même en utilisant `val === val`.

Voici une fonction d'exemple qui vérifie si une valeur donnée est un nombre :

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

Vous pouvez utiliser cette fonction comme suit :

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
