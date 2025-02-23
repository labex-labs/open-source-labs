# Récupération du nom du jour à partir d'un objet Date

Pour récupérer le nom du jour de la semaine à partir d'un objet `Date`, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Date.prototype.toLocaleDateString()` avec l'option `{ weekday: 'long' }` pour récupérer le jour de la semaine.
3. Vous pouvez utiliser le deuxième argument optionnel pour obtenir un nom spécifique à une langue ou le laisser de côté pour utiliser la locale par défaut.

Voici une implémentation d'exemple :

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

Vous pouvez utiliser cette fonction comme ceci :

```js
dayName(new Date()); // 'Saturday'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
