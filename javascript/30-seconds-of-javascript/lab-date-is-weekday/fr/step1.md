# Vérifier si une date est un jour de semaine

Pour vérifier si une date donnée est un jour de semaine, vous pouvez utiliser le extrait de code suivant :

```js
const isWeekday = (date = new Date()) => date.getDay() % 6 !== 0;
```

- Cette fonction utilise `Date.prototype.getDay()` pour obtenir le jour de la semaine sous forme de nombre (de 0 à 6), où dimanche est 0 et samedi est 6.
- Elle vérifie ensuite si le jour de la semaine est différent de 0 (dimanche) ou de 6 (samedi), ce qui signifie qu'il s'agit d'un jour de semaine.
- Si aucune date n'est fournie en argument, la date actuelle est utilisée par défaut.

Utilisation exemple :

```js
isWeekday(); // true (si la date actuelle est un jour de semaine)
isWeekday(new Date(2021, 5, 28)); // true (si la date est un jour de semaine)
```
