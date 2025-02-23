# Wie man in JavaScript ein Array in ein Objekt abbildet

Um in JavaScript ein Array von Objekten in ein Objekt abzubilden, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, um das Array in ein Objekt abzubilden.
3. Verwenden Sie den Parameter `mapKey`, um die Schlüssel des Objekts abzubilden, und den Parameter `mapValue`, um die Werte abzubilden.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie die `objectify`-Funktion verwendet wird, um ein Array von Objekten in ein Objekt abzubilden:

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

Sie können die `objectify`-Funktion dann verwenden, um ein Array von Objekten in ein Objekt auf folgende Weise abzubilden:

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// Mappen Sie das Array von Objekten in ein Objekt, indem Sie die name-Eigenschaft als Schlüssel verwenden
objectify(people, (p) => p.name.toLowerCase());
// Ausgabe: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// Mappen Sie das Array von Objekten in ein Objekt, indem Sie die name-Eigenschaft als Schlüssel und die age-Eigenschaft als Werte verwenden
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// Ausgabe: { john: 42, adam: 39 }
```
