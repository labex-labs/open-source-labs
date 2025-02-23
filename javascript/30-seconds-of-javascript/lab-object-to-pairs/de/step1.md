# Ein Objekt in ein Array von Schlüssel-Wert-Paaren umwandeln

Um ein Objekt in ein Array von Schlüssel-Wert-Paaren umzuwandeln, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Object.entries()`-Methode, um ein Array von Arrays von Schlüssel-Wert-Paaren aus dem Objekt zu erhalten.
3. Erstellen Sie eine Funktion namens `objectToPairs`, die ein Objekt als Argument akzeptiert und das Array von Schlüssel-Wert-Paaren zurückgibt.
4. Rufen Sie die `objectToPairs`-Funktion mit einem Beispielobjekt auf, um die Ausgabe zu testen.

Hier ist eine Beispielimplementierung:

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

Indem Sie diese Schritte ausführen, können Sie ein Objekt mit JavaScript leicht in ein Array von Schlüssel-Wert-Paaren umwandeln.
