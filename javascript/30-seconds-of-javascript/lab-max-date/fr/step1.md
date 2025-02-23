# Trouver la date maximale

Pour trouver la valeur maximale d'une date à partir d'un tableau donné de dates, suivez ces étapes :

1. Ouvrez le Terminal ou SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez la syntaxe de répandue ES6 avec `Math.max()` pour trouver la valeur maximale d'une date.
4. Convertissez la valeur maximale d'une date en un objet `Date` à l'aide du constructeur `Date`.

Voici un extrait de code d'exemple :

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Retourne "2018-03-11T22:00:00.000Z"
```

En suivant ces étapes et en utilisant le code fourni, vous pouvez facilement trouver la valeur maximale d'une date à partir d'un tableau donné de dates.
