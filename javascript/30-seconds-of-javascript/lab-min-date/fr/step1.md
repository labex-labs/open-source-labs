# Comment trouver la date minimale en JavaScript

Pour trouver la valeur de date minimale en JavaScript, vous pouvez utiliser la syntaxe de répandue ES6 avec `Math.min()` et le constructeur `Date`. Voici un extrait de code d'exemple :

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

Pour utiliser cette fonction, créez un tableau d'objets `Date` et passez-le à `minDate()` en utilisant la syntaxe de répandue. Voici un exemple :

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // Retourne un objet `Date` représentant 2016-01-08T22:00:00.000Z
```

En utilisant ce code, vous pouvez facilement trouver la valeur de date minimale en JavaScript.
