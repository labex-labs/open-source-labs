# Comment trier un tableau d'objets en JavaScript

Pour trier un tableau d'objets en JavaScript, vous pouvez utiliser la méthode `Array.prototype.sort()` et la méthode `Array.prototype.reduce()` sur le tableau `props` avec une valeur par défaut de `0`.

Voici une fonction exemple, `orderBy`, qui trie un tableau d'objets en fonction des propriétés et des ordres spécifiés :

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

Pour utiliser cette fonction, passez un tableau d'objets, un tableau de propriétés par lesquelles trier et un tableau optionnel d'ordres. Si aucun tableau `orders` n'est fourni, la fonction triera par `'asc'` par défaut.

Voici quelques exemples d'utilisation de la fonction `orderBy` :

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// trier par nom dans l'ordre croissant et âge dans l'ordre décroissant
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Sortie : [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// trier par nom dans l'ordre croissant et âge dans l'ordre croissant (ordre par défaut)
orderBy(users, ["name", "age"]);
// Sortie : [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
