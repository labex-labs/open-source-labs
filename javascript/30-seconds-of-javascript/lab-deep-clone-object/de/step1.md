# Anweisungen zur tiefen Klonierung eines Objekts

Um ein Objekt tief zu klonen, folgen Sie diesen Schritten:

1. Öffnen Sie eine neue Terminal-/SSH-Instanz und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um primitve Werte, Arrays und Objekte zu klonen, wobei Klasseninstanzen ausgeschlossen werden.
3. Überprüfen Sie, ob das übergebene Objekt `null` ist, und geben Sie im positiven Fall `null` zurück.
4. Verwenden Sie `Object.assign()` und ein leeres Objekt (`{}`), um eine flache Kopie des Ursprungs zu erstellen.
5. Verwenden Sie `Object.keys()` und `Array.prototype.forEach()`, um zu bestimmen, welche Schlüssel-Wert-Paare tief geklont werden müssen.
6. Wenn das Objekt ein `Array` ist, legen Sie die `length` des `clone` auf die Länge des Ursprungs fest und verwenden Sie `Array.from()`, um eine Kopie zu erstellen.
7. Verwenden Sie den folgenden Code, um die tiefe Klonierung zu implementieren:

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

Verwenden Sie den folgenden Code, um Ihre Funktion zur tiefen Klonierung zu testen:

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a!== b, a.obj!== b.obj
```
