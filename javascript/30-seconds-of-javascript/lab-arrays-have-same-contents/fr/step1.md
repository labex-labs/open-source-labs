# Vérification du même contenu dans les tableaux

Pour vérifier si deux tableaux contiennent les mêmes éléments, quelle que soit l'ordre, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Utilisez une boucle `for...of` sur un `Set` créé à partir des valeurs des deux tableaux.
3. Utilisez `Array.prototype.filter()` pour comparer le nombre d'occurrences de chaque valeur distincte dans les deux tableaux.
4. Retournez `false` si les comptes ne correspondent pas pour un élément quelconque, `true` sinon.

Voici le code correspondant :

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

Pour tester la fonction, utilisez le code suivant :

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
