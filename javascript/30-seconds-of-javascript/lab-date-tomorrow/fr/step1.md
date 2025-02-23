# Obtenir la date de demain

Pour pratiquer la programmation, vous pouvez commencer par ouvrir le Terminal/SSH et taper `node`. Une fois que vous avez fait cela, vous pouvez obtenir la date de demain en suivant les étapes suivantes :

1. Utilisez le constructeur `Date` pour obtenir la date actuelle.
2. Incrémentez-la de un en utilisant `Date.prototype.getDate()`.
3. Affectez la valeur au résultat en utilisant `Date.prototype.setDate()`.
4. Utilisez `Date.prototype.toISOString()` pour renvoyer une chaîne de caractères au format `aaaa-mm-jj`.

Voici le code que vous pouvez utiliser :

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

Une fois que vous avez entré ce code, vous pouvez obtenir la date de demain en appelant la fonction `tomorrow()`. Par exemple, si la date d'aujourd'hui est 2018-10-18, la sortie sera `2018-10-19`.
