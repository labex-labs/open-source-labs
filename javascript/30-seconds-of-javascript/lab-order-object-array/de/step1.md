# Wie man ein Array von Objekten in JavaScript sortiert

Um ein Array von Objekten in JavaScript zu sortieren, kannst du die `Array.prototype.sort()`-Methode und die `Array.prototype.reduce()`-Methode auf dem `props`-Array mit einem Standardwert von `0` verwenden.

Hier ist eine Beispiel-Funktion, `orderBy`, die ein Array von Objekten basierend auf den angegebenen Eigenschaften und Reihenfolgen sortiert:

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

Um diese Funktion zu verwenden, übergib ein Array von Objekten, ein Array von Eigenschaften, nach denen sortiert werden soll, und ein optionales Array von Reihenfolgen. Wenn kein `orders`-Array übergeben wird, wird die Funktion standardmäßig nach `'asc'` sortieren.

Hier sind einige Beispiele dafür, wie die `orderBy`-Funktion verwendet werden kann:

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// sortiere nach Namen aufsteigend und Alter absteigend
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Ausgabe: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// sortiere nach Namen aufsteigend und Alter aufsteigend (Standardreihenfolge)
orderBy(users, ["name", "age"]);
// Ausgabe: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
