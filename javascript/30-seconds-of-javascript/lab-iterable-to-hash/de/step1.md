# Umwandeln eines Iterablen in einen Hash

Um ein Iterable (Objekt oder Array) in einen Hash (einen mit Schlüsseln versehenen Datenspeicher) umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Object.values()`, um die Werte des Iterablen zu erhalten.
3. Verwenden Sie `Array.prototype.reduce()`, um über die Werte zu iterieren und ein Objekt zu erstellen, das mit dem Referenzwert als Schlüssel versehen ist.
4. Rufen Sie die `toHash`-Funktion mit dem Iterable und einem optionalen Schlüsselparameter auf, um den Referenzwert anzugeben.

Hier ist eine Beispielimplementierung der `toHash`-Funktion in JavaScript:

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

Sie können die `toHash`-Funktion mit verschiedenen Iterablen und Schlüsseln aufrufen, um verschiedene Hashes zu erstellen. Beispielsweise:

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
