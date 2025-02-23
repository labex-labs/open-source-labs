# Codeübung: Linker Teilstringgenerator

Um alle linken Teilstrings eines gegebenen Strings zu generieren, verwenden Sie die unten bereitgestellte Funktion `leftSubstrGenerator`.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

Um die Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Geben Sie dann die Funktion mit einem String-Argument ein:

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

Die Funktion verwendet `String.prototype.length`, um frühzeitig abzubrechen, wenn der String leer ist, und eine `for...in`-Schleife mit `String.prototype.slice()`, um jeden Teilstring des gegebenen Strings ab dem Anfang zu `yield`.
