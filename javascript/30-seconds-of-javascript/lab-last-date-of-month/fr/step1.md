# Fonction pour retourner la dernière date d'un mois

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction retourne la dernière date du mois pour la date donnée.

Pour y arriver, suivez ces étapes :

1. Utilisez `Date.prototype.getFullYear()` et `Date.prototype.getMonth()` pour obtenir l'année et le mois actuels à partir de la date donnée.
2. Créez une nouvelle date avec l'année et le mois donnés incrémentés de `1`, et le jour défini sur `0` (dernier jour du mois précédent). Vous pouvez utiliser le constructeur `Date` à cette fin.
3. Si aucun argument n'est passé à la fonction, elle utilisera la date actuelle par défaut.
4. Retournez la dernière date du mois au format d'une représentation textuelle de la date.

Voici le code de la fonction :

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

Vous pouvez tester la fonction en l'appelant avec un objet de date comme ceci :

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
