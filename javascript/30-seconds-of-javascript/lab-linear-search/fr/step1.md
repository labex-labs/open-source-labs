# Algorithme de recherche linéaire

Pour pratiquer la programmation, ouvrez le Terminal ou SSH et tapez `node`. L'algorithme de recherche linéaire trouve le premier indice d'un élément donné dans un tableau.

Voici comment il fonctionne :

- Utilisez une boucle `for...in` pour itérer sur les indices du tableau donné.
- Vérifiez si l'élément à l'indice correspondant est égal à `item`.
- Si l'élément est trouvé, renvoyez l'indice. Utilisez l'opérateur unaire `+` pour le convertir d'une chaîne de caractères en nombre.
- Si l'élément n'est pas trouvé après avoir parcouru tout le tableau, renvoyez `-1`.

Voici le code :

```js
const linearSearch = (arr, item) => {
  for (const i in arr) {
    if (arr[i] === item) return +i;
  }
  return -1;
};
```

Pour tester la fonction, appelez-la avec un tableau et une valeur à rechercher :

```js
linearSearch([2, 9, 9], 9); // 1
linearSearch([2, 9, 9], 7); // -1
```
