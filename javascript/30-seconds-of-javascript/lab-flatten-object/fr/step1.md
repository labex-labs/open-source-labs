# Aplatir un objet

Pour aplatir un objet en ajoutant les chemins pour les clés, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursion pour aplatir l'objet.
3. Utilisez `Object.keys()` combinée avec `Array.prototype.reduce()` pour convertir chaque nœud feuille en un nœud de chemin aplati.
4. Si la valeur d'une clé est un objet, appelez la fonction de manière récursive avec le `prefix` approprié pour créer le chemin à l'aide de `Object.assign()`.
5. Sinon, ajoutez la paire clé-valeur préfixée appropriée à l'objet accumulateur.
6. Omettez le second argument, `prefix`, sauf si vous voulez que chaque clé ait un préfixe.

Voici une implémentation d'exemple :

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

Vous pouvez utiliser la fonction `flattenObject` comme ceci :

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
