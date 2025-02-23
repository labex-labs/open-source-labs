# JavaScript-Funktion, um zu überprüfen, ob ein String ein Anagramm ist

Um zu überprüfen, ob ein String ein Anagramm eines anderen Strings ist, verwenden Sie die folgende JavaScript-Funktion. Sie ist groß-/kleinschreibungssensitiv und ignoriert Leerzeichen, Satzzeichen und Sonderzeichen.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

Um die Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Rufen Sie dann die Funktion mit zwei Strings als Argumenten auf:

```js
isAnagram("iceman", "cinema"); // true
```

Die Funktion verwendet `String.prototype.toLowerCase()` und `String.prototype.replace()` mit einem passenden regulären Ausdruck, um unnötige Zeichen zu entfernen. Sie verwendet auch `String.prototype.split()`, `Array.prototype.sort()` und `Array.prototype.join()` auf beiden Strings, um sie zu normalisieren und zu überprüfen, ob ihre normalisierten Formen gleich sind.
