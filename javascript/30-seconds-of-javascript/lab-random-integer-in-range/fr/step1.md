# Comment générer un entier aléatoire dans une plage spécifiée à l'aide de JavaScript

Pour générer un entier aléatoire dans une plage spécifiée à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Math.random()` pour générer un nombre aléatoire compris entre 0 et 1.
3. Ajustez le nombre aléatoire à la plage souhaitée en le multipliant par la différence entre les valeurs maximale et minimale de la plage, puis en ajoutant la valeur minimale au résultat.
4. Utilisez la méthode `Math.floor()` pour arrondir le résultat au plus proche entier.

Voici un extrait de code exemple qui met en œuvre les étapes ci-dessus :

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

Vous pouvez ensuite appeler la fonction `randomIntegerInRange()` avec les valeurs minimales et maximales souhaitées pour générer un entier aléatoire dans cette plage. Par exemple :

```js
randomIntegerInRange(0, 5); // 2
```
