# Transformer les arguments d'une fonction

Pour transformer les arguments d'une fonction, utilisez la fonction `overArgs`, qui crée une nouvelle fonction qui appelle la fonction fournie avec ses arguments transformés.

- Pour transformer les arguments, utilisez `Array.prototype.map()` en combinaison avec l'opérateur de répandage (`...`) et passez les arguments transformés à `fn`.

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- Pour tester la fonction `overArgs`, créez une fonction d'échantillonnage et un tableau de transformations, puis appelez la nouvelle fonction avec des arguments.

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
