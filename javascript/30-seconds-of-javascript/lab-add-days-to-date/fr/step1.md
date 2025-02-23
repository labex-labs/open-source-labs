# Fonction pour ajouter des jours à une date

Voici une fonction qui peut calculer la date de `n` jours à partir de la date donnée et renvoyer sa représentation sous forme de chaîne de caractères.

Pour utiliser la fonction, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Date` pour créer un objet `Date` à partir du premier argument.
3. Utilisez `Date.prototype.getDate()` et `Date.prototype.setDate()` pour ajouter `n` jours à la date donnée.
4. Utilisez `Date.prototype.toISOString()` pour renvoyer une chaîne de caractères au format `yyyy-mm-dd`.

Voici le code de la fonction :

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

Vous pouvez tester la fonction à l'aide des exemples suivants :

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
