# Algorithme pour compactifier un objet

Pour supprimer profondément toutes les valeurs fausses d'un objet ou d'un tableau, utilisez l'algorithme suivant :

1. Utilisez la récursion pour appeler la fonction `compactObject()` sur chaque objet ou tableau imbriqué.
2. Initialisez les données itérables à l'aide de `Array.isArray()`, `Array.prototype.filter()` et `Boolean()`. Cela est fait pour éviter les tableaux creux.
3. Utilisez `Object.keys()` et `Array.prototype.reduce()` pour itérer sur chaque clé avec une valeur initiale appropriée.
4. Utilisez `Boolean()` pour déterminer la véracité de la valeur de chaque clé et l'ajoutez à l'accumulateur si elle est véridique.
5. Utilisez `typeof` pour déterminer si une valeur donnée est un `objet` et appelez la fonction à nouveau pour la compactifier profondément.

Voici le code pour la fonction `compactObject()` :

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

Pour utiliser cette fonction, passez un objet ou un tableau en tant qu'argument à `compactObject()`. La fonction renverra un nouvel objet ou tableau avec toutes les valeurs fausses supprimées.

Par exemple :

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
