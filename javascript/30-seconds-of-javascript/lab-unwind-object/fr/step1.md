# Unwind Object Function

Pour dérouler (unwind) un objet en fonction de sa propriété de type tableau, utilisez la fonction `unwind`.

- Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.
- La fonction utilise la déconstruction d'objets pour exclure la paire clé-valeur pour la `clé` spécifiée de l'objet.
- Ensuite, elle utilise `Array.prototype.map()` pour les valeurs de la `clé` donnée pour créer un tableau d'objets.
- Chaque objet contient les valeurs de l'objet original, sauf pour `clé` qui est mappée à ses valeurs individuelles.

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

Utilisation de l'exemple :

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
