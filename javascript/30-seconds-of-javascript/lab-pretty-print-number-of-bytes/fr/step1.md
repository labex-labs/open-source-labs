# Convertir des octets en chaîne lisible par l'homme

Pour convertir un nombre d'octets en une chaîne de caractères lisible par l'homme, utilisez la fonction `prettyBytes()`. Voici quelques points à garder à l'esprit :

- La fonction utilise un tableau dictionnaire d'unités qui peut être accédé en fonction de l'exposant.
- Vous pouvez utiliser le deuxième argument, `precision`, pour tronquer le nombre à un certain nombre de chiffres. La valeur par défaut est `3`.
- Vous pouvez utiliser le troisième argument, `addSpace`, pour ajouter un espace entre le nombre et l'unité. La valeur par défaut est `true`.
- La fonction renvoie la chaîne formatée en la construisant, en tenant compte des options fournies et du fait que le nombre soit négatif ou non.

Voici le code de la fonction `prettyBytes()` :

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

Et voici quelques exemples d'utilisation de la fonction `prettyBytes()` :

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
