# Fonction pour Combiner des Tableaux d'Objets sur la Base d'une Clé Spécifiée

Pour combiner deux tableaux d'objets sur la base d'une clé spécifique, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` avec un accumulateur d'objet pour combiner tous les objets des deux tableaux sur la base de la `prop` donnée.
3. Utilisez `Object.values()` pour convertir l'objet résultant en un tableau et le retourner.

Voici la fonction que vous pouvez utiliser :

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

Voici un exemple d'utilisation de cette fonction :

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
