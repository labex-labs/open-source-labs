# Code zum Iterieren über die Schlüssel eines Objekts

Um eine Liste aller Schlüssel eines gegebenen Objekts zu generieren, verwenden Sie die folgenden Schritte:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Definieren Sie eine Generator-Funktion namens `walk`, die ein Objekt und ein Array von Schlüsseln akzeptiert. Verwenden Sie Rekursion, um alle Schlüssel des Objekts zu iterieren.

3. Innerhalb der `walk`-Funktion verwenden Sie eine `for...of`-Schleife und `Object.keys()`, um über die Schlüssel des Objekts zu iterieren.

4. Verwenden Sie `typeof`, um zu überprüfen, ob jeder Wert im gegebenen Objekt selbst ein Objekt ist. Wenn der Wert ein Objekt ist, verwenden Sie den `yield*`-Ausdruck, um rekursiv an die gleiche Generator-Funktion, `walk`, zu delegieren und den aktuellen `key` an das Array von Schlüsseln anzuhängen.

5. Andernfalls `yield` ein Array von Schlüsseln, das den aktuellen Pfad und den Wert des gegebenen `key` repräsentiert.

6. Verwenden Sie den `yield*`-Ausdruck, um an die `walk`-Generator-Funktion zu delegieren.

Hier ist der Code:

```js
const walkThrough = function* (obj) {
  const walk = function* (x, previous = []) {
    for (let key of Object.keys(x)) {
      if (typeof x[key] === "object") yield* walk(x[key], [...previous, key]);
      else yield [[...previous, key], x[key]];
    }
  };
  yield* walk(obj);
};
```

Um den Code zu testen, erstellen Sie ein Objekt und verwenden Sie die `walkThrough`-Funktion, um eine Liste aller seiner Schlüssel zu generieren:

```js
const obj = {
  a: 10,
  b: 20,
  c: {
    d: 10,
    e: 20,
    f: [30, 40]
  },
  g: [
    {
      h: 10,
      i: 20
    },
    {
      j: 30
    },
    40
  ]
};
[...walkThrough(obj)];
/*
[
  [['a'], 10],
  [['b'], 20],
  [['c', 'd'], 10],
  [['c', 'e'], 20],
  [['c', 'f', '0'], 30],
  [['c', 'f', '1'], 40],
  [['g', '0', 'h'], 10],
  [['g', '0', 'i'], 20],
  [['g', '1', 'j'], 30],
  [['g', '2'], 40]
]
*/
```
