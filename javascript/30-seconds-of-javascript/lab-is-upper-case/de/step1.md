# Funktion, um zu überprüfen, ob ein String in Großbuchstaben geschrieben ist

Um zu überprüfen, ob ein String in Großbuchstaben geschrieben ist, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein.
3. Verwenden Sie die Funktion `isUpperCase()`, um den gegebenen String mithilfe von `String.prototype.toUpperCase()` in Großbuchstaben umzuwandeln und ihn mit dem ursprünglichen String zu vergleichen.
4. Die Funktion wird `true` zurückgeben, wenn der String in Großbuchstaben geschrieben ist, und `false`, wenn er es nicht ist.

Hier ist ein Beispielcode:

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
