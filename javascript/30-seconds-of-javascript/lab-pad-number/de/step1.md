# Wie man in JavaScript eine Zahl auffüllt

Um in JavaScript eine Zahl aufzufüllen, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `String.prototype.padStart()`-Methode, um die Zahl auf die angegebene Länge aufzufüllen, nachdem Sie sie in einen String umgewandelt haben.
3. Die unten stehende `padNumber()`-Funktion demonstriert diesen Ansatz.
4. Übergeben Sie die Zahl und die gewünschte Länge als Argumente an die Funktion.
5. Die Funktion gibt die aufgefüllte Zahl als String zurück.

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

Beispielverwendung:

```js
padNumber(1234, 6); // '001234'
```
