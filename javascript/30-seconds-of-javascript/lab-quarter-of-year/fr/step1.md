# Fonction pour déterminer le trimestre de l'année

Pour déterminer le trimestre de l'année, utilisez la fonction `quarterOfYear()`. Cette fonction prend un argument `date` optionnel et renvoie un tableau avec le trimestre et l'année auquel appartient la date fournie.

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node`. Ensuite, copiez et collez le code suivant :

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

La fonction `quarterOfYear()` utilise les étapes suivantes pour calculer le trimestre et l'année :

- Utilise `Date.prototype.getMonth()` pour obtenir le mois actuel dans la plage (0, 11), ajoute `1` pour le mapper dans la plage (1, 12).
- Utilise `Math.ceil()` et divise le mois par `3` pour obtenir le trimestre actuel.
- Utilise `Date.prototype.getFullYear()` pour obtenir l'année à partir de la `date` donnée.
- Omet l'argument `date` pour utiliser la date actuelle par défaut.

Voici quelques exemples d'utilisation de la fonction `quarterOfYear()` :

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
