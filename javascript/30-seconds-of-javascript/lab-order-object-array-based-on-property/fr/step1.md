# Comment ordonner un tableau d'objets selon l'ordre d'une propriété

Pour ordonner un tableau d'objets selon l'ordre d'une propriété, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` pour créer un objet à partir du tableau `order` avec les valeurs comme clés et leur index original comme valeur.
3. Utilisez `Array.prototype.sort()` pour trier le tableau donné, en sautant les éléments pour lesquels `prop` est vide ou n'est pas dans le tableau `order`.

Voici un extrait de code d'exemple pour ordonner un tableau d'objets selon l'ordre d'une propriété :

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

Vous pouvez utiliser la fonction `orderWith` pour ordonner un tableau d'objets selon l'ordre d'une propriété. Par exemple :

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
