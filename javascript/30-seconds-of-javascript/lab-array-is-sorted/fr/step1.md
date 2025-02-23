# Code Practice: Vérifier si un tableau est trié

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction pour vérifier si un tableau numérique est trié :

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

Pour l'utiliser, passez un tableau de nombres à `isSorted()`. La fonction retournera `1` si le tableau est trié par ordre croissant, `-1` s'il est trié par ordre décroissant et `0` s'il n'est pas trié.

Voici quelques exemples :

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
