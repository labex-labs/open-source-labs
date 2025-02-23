# Fonction pour calculer la date de 'n' jours à partir d'aujourd'hui

Pour calculer la date de 'n' jours à partir d'aujourd'hui, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez 'node' pour commencer à pratiquer la programmation.
- Utilisez le constructeur `Date` pour obtenir la date actuelle.
- Utilisez `Math.abs()` et `Date.prototype.getDate()` pour mettre à jour la date en conséquence.
- Définissez le résultat en utilisant `Date.prototype.setDate()`.
- Utilisez `Date.prototype.toISOString()` pour retourner une chaîne au format `aaaa-mm-jj`.

Voici le code :

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

Utilisation de l'exemple :

```js
daysFromNow(5); // Sortie : 2020-10-13 (si la date actuelle est 2020-10-08)
```
