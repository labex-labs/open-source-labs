# Code pour vérifier si une année est bissextile

Pour vérifier si une année donnée `year` est bissextile, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à coder.
3. Utilisez le constructeur `Date` et définissez la date au 29 février de l'année donnée `year`.
4. Vérifiez si le mois est égal à `1` en utilisant `Date.prototype.getMonth()`.
5. Utilisez le extrait de code suivant pour vérifier si une année est bissextile :

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

Voici un exemple d'utilisation de ce code :

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
