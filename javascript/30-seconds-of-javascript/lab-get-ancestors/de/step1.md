# Elementvorgänger abrufen

Um die Vorgänger eines Elements von der Dokumentenwurzel bis zum angegebenen Element abzurufen, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Node.parentNode` und eine `while`-Schleife, um den Vorgängerbaum des Elements hinauf zu bewegen.
3. Verwenden Sie `Array.prototype.unshift()`, um jeden neuen Vorgänger am Anfang des Arrays hinzuzufügen.

Hier ist ein Beispielcode, der die obigen Schritte implementiert:

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

Um die Vorgänger eines bestimmten Elements abzurufen, verwenden Sie die `querySelector()`-Methode, um das Element auszuwählen und es als Argument an die `getAncestors()`-Funktion zu übergeben. Beispiel:

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

Dies wird ein Array aller Vorgänger des angegebenen Elements in der Reihenfolge von der Dokumentenwurzel bis zum Element selbst zurückgeben.
