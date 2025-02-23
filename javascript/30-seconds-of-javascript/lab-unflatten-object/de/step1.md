# Wie man in JavaScript ein Objekt entflacht

Um in JavaScript ein Objekt mit Pfaden für Schlüssel zu entflachen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie die geschachtelte `Array.prototype.reduce()`, um den flachen Pfad in einen Blattknoten umzuwandeln.

3. Verwenden Sie `String.prototype.split()`, um jeden Schlüssel mit einem Punkt als Trennzeichen zu teilen und `Array.prototype.reduce()`, um gegen die Schlüssel Objekte hinzuzufügen.

4. Wenn der aktuelle Akkumulator bereits einen Wert für einen bestimmten Schlüssel enthält, geben Sie seinen Wert als nächsten Akkumulator zurück.

5. Andernfalls fügen Sie das passende Schlüssel-Wert-Paar dem Akkumulatorobjekt hinzu und geben Sie den Wert als Akkumulator zurück.

Hier ist der Code für die `unflattenObject`-Funktion:

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

Sie können die `unflattenObject`-Funktion verwenden, um in JavaScript ein Objekt zu entflachen:

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
