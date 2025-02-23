# Wie man ein Array anhand einer Funktion in zwei teilt

Um ein Array anhand einer bereitgestellten Funktion in zwei zu teilen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, um ein Array aus zwei Arrays zu erstellen.
3. Verwenden Sie `Array.prototype.push()`, um Elemente, für die `fn` `true` zurückgibt, der ersten und Elemente, für die `fn` `false` zurückgibt, der zweiten Array hinzuzufügen.

Hier ist der Code, den Sie verwenden können:

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

Um diesen Code zu testen, können Sie folgendes Beispiel verwenden:

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

Dies wird ein Array aus zwei Arrays zurückgeben, wobei das erste Array alle Elemente enthält, für die die bereitgestellte Funktion `true` zurückgibt, und das zweite Array alle Elemente enthält, für die die bereitgestellte Funktion `false` zurückgibt.
