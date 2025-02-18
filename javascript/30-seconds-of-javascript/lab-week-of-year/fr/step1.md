# Obtenir la semaine de l'année à partir d'une date en JavaScript

Pour obtenir la semaine de l'année indexée à partir de zéro qui correspond à une date en JavaScript, suivez ces étapes :

1. Créez une fonction `weekOfYear` qui prend un paramètre `date`.
2. Utilisez le constructeur `Date` et la méthode `Date.prototype.getFullYear()` pour obtenir le premier jour de l'année sous forme d'un objet `Date`.
3. Utilisez les méthodes `Date.prototype.setDate()`, `Date.prototype.getDate()` et `Date.prototype.getDay()` ainsi que l'opérateur modulo (`%`) pour obtenir le premier lundi de l'année.
4. Soustrayez le premier lundi de l'année de la `date` donnée et divisez le résultat par le nombre de millisecondes dans une semaine.
5. Utilisez `Math.round()` pour obtenir la semaine de l'année indexée à partir de zéro correspondant à la `date` donnée.
6. Si la `date` donnée est antérieure au premier lundi de l'année, `-0` est retourné.

Voici le code :

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

Pour utiliser la fonction `weekOfYear`, appelez - la simplement en lui passant un objet `Date` comme paramètre :

```js
weekOfYear(new Date("2021-06-18")); // 23
```

Cela retournera la semaine de l'année indexée à partir de zéro qui correspond à la date donnée, qui dans ce cas est `23`.
