# Comment vérifier si une date est antérieure à une autre en JavaScript

Pour vérifier si une date est antérieure à une autre en JavaScript, vous pouvez utiliser l'opérateur inférieur (`<`). Voici un exemple de fonction qui prend deux dates en paramètre et renvoie une valeur booléenne indiquant si la première date est antérieure à la seconde :

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

Vous pouvez utiliser cette fonction pour vérifier si une date spécifique est antérieure à une autre date en passant deux objets `Date` en tant qu'arguments. Par exemple :

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
