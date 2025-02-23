# Comment créer un objet Date à partir d'un timestamp Unix

Pour créer un objet `Date` à partir d'un timestamp Unix, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Multipliez le timestamp par `1000` pour le convertir en millisecondes.
3. Utilisez le constructeur `Date` pour créer un nouvel objet `Date`.

Voici un extrait de code d'exemple :

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

Vous pouvez utiliser cette fonction pour convertir un timestamp Unix en objet `Date` comme ceci :

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
