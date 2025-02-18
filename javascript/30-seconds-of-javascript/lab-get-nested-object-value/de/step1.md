# Wie man verschachtelte Objekteigenschaften aus Pfadzeichenfolgen abruft

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die folgende Funktion ruft eine Reihe von Eigenschaften aus einem Objekt mithilfe von Selektoren ab, die in einer Pfadzeichenfolge angegeben sind. Um dies zu erreichen, befolgen Sie diese Schritte:

1. Verwenden Sie `Array.prototype.map()`, um durch jeden Selektoren zu iterieren, und wenden Sie `String.prototype.replace()` an, um eckige Klammern durch Punkte zu ersetzen.
2. Verwenden Sie `String.prototype.split()`, um jeden Selektoren in ein Array von Zeichenfolgen aufzuteilen.
3. Verwenden Sie `Array.prototype.filter()`, um alle leeren Werte zu entfernen.
4. Verwenden Sie `Array.prototype.reduce()`, um den von jedem Selektoren angegebenen Wert abzurufen.

Hier ist die Funktion:

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

Sie können diese Funktion verwenden, um Werte aus einem verschachtelten Objekt mithilfe einer Pfadzeichenfolge abzurufen. Hier ist ein Beispiel:

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
