# Générateur de plage de dates

Pour générer toutes les dates dans une plage donnée avec un pas donné, utilisez le code suivant dans le Terminal/SSH et tapez `node` :

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

Cela crée un générateur qui utilise une boucle `while` pour itérer de `start` à `end`, utilise le constructeur `Date` pour renvoyer chaque date dans la plage et incrémente de `step` jours à l'aide de `Date.prototype.getDate()` et `Date.prototype.setDate()`.

Pour utiliser la valeur par défaut de `1` pour `step`, omettez le troisième argument.

Voici un exemple de manière d'utiliser le `dateRangeGenerator` :

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
