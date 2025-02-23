# Fonction JavaScript pour obtenir le nombre de jours dans un mois

Pour trouver le nombre de jours dans un mois spécifique d'une année donnée à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez une fonction nommée `daysInMonth` qui prend deux paramètres : `year` (année) et `month` (mois).
3. À l'intérieur de la fonction `daysInMonth`, utilisez le constructeur `Date` pour créer un objet de date à partir de l'`année` et du `mois` donnés.
4. Définissez le paramètre `jours` sur `0` pour obtenir le dernier jour du mois précédent, car les mois sont indexés à partir de zéro.
5. Utilisez `Date.prototype.getDate()` pour renvoyer le nombre de jours dans le `mois` donné.
6. Retournez le nombre de jours à partir de la fonction `daysInMonth`.

Voici le code JavaScript pour la fonction `daysInMonth` :

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

Vous pouvez utiliser la fonction `daysInMonth` pour obtenir le nombre de jours dans n'importe quel mois d n'importe quelle année, comme le montrent ces exemples :

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
