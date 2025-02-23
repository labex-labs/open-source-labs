# Vérifier si une valeur est un symbole en JavaScript

Pour vérifier si une valeur est un type primitif symbole en JavaScript, vous pouvez utiliser l'opérateur `typeof`. Voici un extrait de code d'exemple que vous pouvez utiliser :

```js
const isSymbol = (val) => typeof val === "symbol";
```

Vous pouvez appeler la fonction `isSymbol` et passer un symbole en tant qu'argument pour vérifier si elle renvoie `true`. Voici un exemple :

```js
isSymbol(Symbol("x")); // true
```
