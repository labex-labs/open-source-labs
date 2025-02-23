# Vérifier si une date est un week-end

Pour vérifier si une date donnée est un week-end, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez la méthode `Date.prototype.getDay()` pour obtenir le jour de la semaine sous forme de nombre (0-6), le dimanche étant 0 et le samedi étant 6.
- Vérifiez si le jour est un week-end en utilisant l'opérateur modulo (`%`) et en le comparant à 0 ou 6.
- Omettez l'argument `d` pour utiliser la date actuelle comme valeur par défaut.

Voici un extrait de code exemple que vous pouvez utiliser :

```js
const isWeekend = (d = new Date()) => d.getDay() % 6 === 0;
```

Pour tester la fonction, appelez-la simplement sans aucun argument :

```js
isWeekend(); // true ou false (selon la date actuelle)
```

Cela renverra `true` si la date actuelle est un week-end (samedi ou dimanche) et `false` dans le cas contraire.
