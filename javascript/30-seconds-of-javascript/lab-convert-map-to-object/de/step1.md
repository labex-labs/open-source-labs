# Anweisungen zur Umwandlung einer Map in ein Objekt in JavaScript

Um eine JavaScript-`Map` in ein Objekt umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Map.prototype.entries()`-Methode, um die `Map` in ein Array von Schlüssel-Wert-Paaren umzuwandeln.
3. Verwenden Sie die `Object.fromEntries()`-Methode, um das Array in ein Objekt umzuwandeln.

Hier ist ein Beispielcodeausschnitt zur Umwandlung einer `Map` in ein Objekt:

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

Um die Funktion zu testen, können Sie ausführen:

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
