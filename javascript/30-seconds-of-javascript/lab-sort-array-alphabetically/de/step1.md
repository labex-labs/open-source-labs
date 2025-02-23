# Wie man ein Array alphabetisch nach einer angegebenen Eigenschaft in JavaScript sortiert

Um ein Array von Objekten alphabetisch nach einer angegebenen Eigenschaft in JavaScript zu sortieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.sort()`, um das Array nach der angegebenen Eigenschaft zu sortieren.
3. Verwenden Sie `String.prototype.localeCompare()`, um die Werte für die angegebene Eigenschaft zu vergleichen.

Hier ist ein Beispielcodeausschnitt, den Sie verwenden können:

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

Sie können die `alphabetical`-Funktion mit einem Array von Objekten und der Getter-Funktion aufrufen, die die zu sortierende Eigenschaft zurückgibt. Hier ist ein Beispiel für die Verwendung:

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
