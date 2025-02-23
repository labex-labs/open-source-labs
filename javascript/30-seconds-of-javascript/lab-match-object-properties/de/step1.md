# Wie man Objekteigenschaften in JavaScript vergleicht

Um zwei Objekte zu vergleichen und zu überprüfen, ob sie die gleichen Eigenschaftswerte haben, verwenden Sie die `matches`-Funktion. Hier ist, wie man sie verwendet:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu codieren.
2. Kopieren Sie und fügen Sie den Code der `matches`-Funktion in Ihre JavaScript-Datei ein.
3. Rufen Sie die Funktion auf und übergeben Sie zwei Objekte als Argumente. Das erste Objekt ist das, das Sie vergleichen möchten, und das zweite Objekt ist das, mit dem Sie es vergleichen möchten.

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

Die `matches`-Funktion verwendet `Object.keys()`, um alle Schlüssel des zweiten Objekts zu erhalten, und überprüft dann, ob alle Schlüssel im ersten Objekt existieren und die gleichen Werte haben, indem `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` und strenge Vergleich verwendet werden.
