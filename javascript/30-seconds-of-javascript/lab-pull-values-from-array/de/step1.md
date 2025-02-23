# Wie man in JavaScript Werte aus einem Array extrahiert

Um bestimmte Werte aus einem Array in JavaScript zu extrahieren, können Sie die Methoden `Array.prototype.filter()` und `Array.prototype.includes()` verwenden. Hier ist, wie Sie es tun können:

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

Die `pull`-Funktion nimmt ein Array und ein oder mehrere Argumente entgegen, die die zu entfernenden Werte darstellen. Die Funktion erstellt dann ein neues Array, indem sie die mithilfe von `Array.prototype.filter()` angegebenen Werte herausfiltert. Anschließend mutiert sie das ursprüngliche Array, indem sie seine Länge auf `0` setzt und es nur mit den extrahierten Werten mithilfe von `Array.prototype.push()` wieder füllt.

Hier ist ein Beispiel dafür, wie Sie die `pull`-Funktion verwenden können:

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

In diesem Beispiel entfernt die `pull`-Funktion alle Vorkommen von `'a'` und `'c'` aus dem `myArray`-Array und gibt ein neues Array mit nur den Werten `'b'` und `'b'` zurück.
