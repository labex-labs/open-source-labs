# Übereinstimmen von Objekteigenschaften mit einer Funktion

Um zu beginnen, die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion vergleicht zwei Objekte und überprüft, ob das erste Objekt äquivalente Eigenschaftswerte wie das zweite enthält. Dies geschieht basierend auf einer bereitgestellten Funktion.

Um diese Funktion zu verwenden, folgen Sie diesen Schritten:

- Verwenden Sie `Object.keys()`, um alle Schlüssel des zweiten Objekts abzurufen.
- Verwenden Sie `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` und die bereitgestellte Funktion, um zu bestimmen, ob alle Schlüssel im ersten Objekt existieren und äquivalente Werte haben.
- Wenn keine Funktion bereitgestellt wird, werden die Werte mit dem Gleichheitsoperator verglichen.

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

Dieses Beispiel überprüft, ob die beiden Objekte äquivalente Werte für die `greeting`-Eigenschaft haben. Es verwendet die `isGreeting`-Funktion, um sicherzustellen, dass beide Werte gültige Begrüßungen sind.
