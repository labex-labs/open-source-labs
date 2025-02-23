# Index von Teilzeichenketten

Um alle Vorkommen einer Teilzeichenkette in einer gegebenen Zeichenkette zu finden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die integrierte Methode `Array.prototype.indexOf()`, um nach `searchValue` in `str` zu suchen.
3. Verwenden Sie `yield`, um den Index zurückzugeben, wenn der Wert gefunden wurde, und aktualisieren Sie den Index `i`.
4. Verwenden Sie eine `while-Schleife`, die den Generator sofort beendet, sobald der Wert, der von `Array.prototype.indexOf()` zurückgegeben wird, `-1` ist.

Hier ist ein Beispielcode, um die obigen Schritte umzusetzen:

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

Sie können die Funktion mit dem folgenden Code testen:

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
