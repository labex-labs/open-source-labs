# Wie man einen verschachtelten Wert in einem Objekt mithilfe eines Arrays von Schlüsseln abruft

Um einen bestimmten Wert aus einem verschachtelten JSON-Objekt abzurufen, können Sie die `deepGet`-Funktion verwenden. Diese Funktion nimmt ein Objekt und ein Array von Schlüsseln entgegen und gibt den Zielwert zurück, wenn er im Objekt vorhanden ist.

Um die `deepGet`-Funktion zu verwenden:

- Erstellen Sie ein Array der Schlüssel, die Sie aus dem verschachtelten JSON-Objekt abrufen möchten.
- Rufen Sie die `deepGet`-Funktion mit dem Objekt und dem Array der Schlüssel auf.
- Die Funktion wird den Zielwert zurückgeben, wenn er vorhanden ist, oder `null`, wenn er nicht vorhanden ist.

Hier ist der Code für die `deepGet`-Funktion:

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

Und hier ist ein Beispiel dafür, wie man die `deepGet`-Funktion verwendet:

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // gibt 3 zurück
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // gibt null zurück
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
