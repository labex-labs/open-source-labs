# Wie man in JavaScript jedes Wort großschreibt

Um in JavaScript jedes Wort in einem String großzuschreiben, kannst du die `String.prototype.replace()`-Methode verwenden, um das erste Zeichen jedes Wortes zu finden, und dann die `String.prototype.toUpperCase()`-Methode, um es großzuschreiben.

Hier ist ein Beispiel-Codeausschnitt, den du verwenden kannst:

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

Um diese Funktion zu verwenden, gib als Argument den String ein, den du großschreiben möchtest, wie folgt:

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

Dies wird den großgeschriebenen String 'Hello World!' zurückgeben.
