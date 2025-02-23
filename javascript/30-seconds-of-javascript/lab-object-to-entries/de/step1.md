# Umwandeln eines Objekts in ein Array von Schlüssel-Wert-Paaren

Um ein Objekt in ein Array von Schlüssel-Wert-Paaren umzuwandeln, verwenden Sie die `Object.keys()`-Methode und die `Array.prototype.map()`-Methode. Dies wird über die Schlüssel des Objekts iterieren und ein Array mit Schlüssel-Wert-Paaren erzeugen. Alternativ können Sie die `Object.entries()`-Methode verwenden, die eine ähnliche Funktionalität bietet.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie man ein Objekt in ein Array von Schlüssel-Wert-Paaren umwandelt:

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

Sie können die `objectToEntries()`-Funktion verwenden, um ein Objekt in ein Array von Schlüssel-Wert-Paaren zu konvertieren, wie folgt:

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
