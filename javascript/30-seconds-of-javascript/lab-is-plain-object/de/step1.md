# Überprüfen, ob ein Wert ein einfaches Objekt ist

Um zu überprüfen, ob ein Wert ein einfaches Objekt ist, führen Sie die folgenden Schritte aus:

- Überprüfen Sie, ob der Wert wahrheitsfähig ist.
- Verwenden Sie `typeof`, um zu überprüfen, ob es ein Objekt ist.
- Verwenden Sie `Object.prototype.constructor`, um sicherzustellen, dass der Konstruktor gleich `Object` ist.

Verwenden Sie den folgenden Code, um diese Überprüfung umzusetzen:

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

Sie können diese Funktion mit den folgenden Beispielen testen:

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
