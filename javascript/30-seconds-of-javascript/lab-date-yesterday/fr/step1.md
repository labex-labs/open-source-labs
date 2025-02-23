# Obtenir la date d'hier au format yyyy - mm - dd

Pour obtenir la date d'hier au format `yyyy - mm - dd`, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Date` pour obtenir la date actuelle.
3. Décrémentez la date d'un jour en utilisant `Date.prototype.getDate()`.
4. Définissez la date décrémentée en utilisant `Date.prototype.setDate()`.
5. Utilisez `Date.prototype.toISOString()` pour retourner une chaîne de caractères au format `yyyy - mm - dd`.
6. Appelez la fonction `yesterday()` pour obtenir la date d'hier.

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // retourne "2018-10-17" (si la date actuelle est 2018-10-18)
```

En suivant ces étapes, vous serez capable de récupérer la date d'hier de manière claire et concise.
