# Générer un tableau d'entiers aléatoires dans une plage spécifique

Pour générer un tableau d'entiers aléatoires dans une plage spécifique, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.from()` pour créer un tableau vide de la longueur souhaitée.
3. Utilisez `Math.random()` pour générer des nombres aléatoires et les mapper à la plage spécifiée. Utilisez `Math.floor()` pour les convertir en entiers.
4. La fonction `randomIntArrayInRange()` prend trois arguments : `min`, `max` et un argument optionnel `n` (valeur par défaut est 1).
5. Appelez la fonction `randomIntArrayInRange()` avec les valeurs souhaitées de `min`, `max` et `n` pour générer le tableau d'entiers aléatoires.

Voici le code :

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

Utilisation exemple :

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
