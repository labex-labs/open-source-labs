# Fonction pour obtenir la taille d'un tableau, d'un objet ou d'une chaîne de caractères

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node`. Cette fonction obtient la taille d'un tableau, d'un objet ou d'une chaîne de caractères.

Pour l'utiliser :

- Déterminez le type de `val` (`array`, `object` ou `string`).
- Utilisez la propriété `Array.prototype.length` pour les tableaux.
- Utilisez la valeur `length` ou `size` si disponible, ou le nombre de clés pour les objets.
- Pour les chaînes de caractères, utilisez la `size` d'un objet [`Blob`](https://developer.mozilla.org/fr/docs/Web/API/Blob) créé à partir de `val`.

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

Exemples :

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
