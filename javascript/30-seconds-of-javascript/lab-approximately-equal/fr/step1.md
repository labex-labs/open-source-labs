# Vérification de l'égalité approximative de nombres en JavaScript

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Ce code vérifie si deux nombres sont approximativement égaux l'un à l'autre. Pour ce faire :

- Utilisez la méthode `Math.abs()` pour comparer la différence absolue des deux valeurs à `epsilon`.
- Si vous ne fournissez pas un troisième argument, `epsilon`, la fonction utilisera une valeur par défaut de `0,001`.

Voici le code :

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

Pour tester la fonction, vous pouvez l'appeler avec deux nombres en arguments, comme ceci :

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

Cela retournera `true` car `Math.PI / 2.0` est approximativement égal à `1,5708` avec un epsilon de `0,001`.
