# Fonction pour vérifier si un tableau est contenu dans un autre tableau

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`. Cette fonction vérifie si tous les éléments du premier tableau sont présents dans le second tableau, quelle que soit leur ordre.

Voici les étapes à suivre :

1. Utilisez une boucle `for...of` pour itérer sur un `Set` créé à partir du premier tableau.
2. Appliquez `Array.prototype.some()` pour vérifier si toutes les valeurs distinctes sont présentes dans le second tableau.
3. Utilisez `Array.prototype.filter()` pour comparer le nombre d'occurrences de chaque valeur distincte dans les deux tableaux.
4. Si le compte de tout élément est supérieur dans le premier tableau que dans le second, renvoyez `false`. Sinon, renvoyez `true`.

Consultez le code ci-dessous pour voir comment cela fonctionne :

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

Pour tester la fonction, utilisez le code suivant :

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
