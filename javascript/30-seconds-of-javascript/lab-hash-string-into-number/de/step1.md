# Wie man in JavaScript einen String in eine Zahl hasht

Um in JavaScript einen Eingabestring in eine Ganzzahl zu hashen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Methoden `String.prototype.split()` und `Array.prototype.reduce()`, um einen Hash des Eingabestrings zu erstellen, wobei Sie Bitverschiebungen nutzen.
3. Hier ist der Code für die `sdbm`-Funktion, die den Hash-Algorithmus implementiert:

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. Um die Funktion zu testen, rufen Sie sie mit einem String-Argument auf:

```js
sdbm("name"); // -3521204949
```

Dies wird den Hash-Wert für den Eingabestring "name" zurückgeben.
