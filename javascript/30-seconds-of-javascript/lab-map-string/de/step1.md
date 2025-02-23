# Funktion zum Abbilden von Zeichen in einer Zeichenfolge

Um diese Funktion zum Abbilden von Zeichen in einer Zeichenfolge zu verwenden, führen Sie die folgenden Schritte aus:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
- Verwenden Sie `String.prototype.split()` und `Array.prototype.map()`, um die bereitgestellte Funktion `fn` für jedes Zeichen in der gegebenen Zeichenfolge aufzurufen.
- Verwenden Sie `Array.prototype.join()`, um das Array von Zeichen zu einer neuen Zeichenfolge zusammenzufügen.
- Die Callback-Funktion `fn` nimmt drei Argumente entgegen: das aktuelle Zeichen, den Index des aktuellen Zeichens und die Zeichenfolge, auf der `mapString` aufgerufen wurde.

Hier ist der Funktionscode:

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

Beispielverwendung:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
