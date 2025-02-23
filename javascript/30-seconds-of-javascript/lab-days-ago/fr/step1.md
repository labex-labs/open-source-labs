# Fonction JavaScript pour calculer le nombre de jours auparavant

Voici une fonction JavaScript qui calcule la date il y a `n` jours à partir d'aujourd'hui et la renvoie sous forme de chaîne de caractères au format `aaaa-mm-jj` :

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

Voici comment elle fonctionne :

- Le constructeur `Date` est utilisé pour obtenir la date actuelle.
- La fonction `Math.abs()` est utilisée pour s'assurer que le nombre de jours est positif.
- La fonction `Date.prototype.getDate()` est utilisée pour obtenir le jour du mois de la date actuelle.
- La fonction `Date.prototype.setDate()` est utilisée pour mettre à jour la date en conséquence.
- La date résultante est renvoyée sous forme de chaîne de caractères au format `aaaa-mm-jj` à l'aide de la fonction `Date.prototype.toISOString()`.

Exemple d'utilisation :

```js
daysAgo(20); // "2020-09-16" (si la date actuelle est 2020-10-06)
```
