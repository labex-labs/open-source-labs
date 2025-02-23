# Wie man in JavaScript über die eigenen Eigenschaften eines Objekts iteriert

Um über die eigenen Eigenschaften eines Objekts zu iterieren und die Programmierung zu üben, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal oder SSH.
2. Geben Sie `node` ein, um eine neue Node.js-Sitzung zu starten.
3. Verwenden Sie die `Object.keys()`-Methode, um ein Array der eigenen Eigenschaften des Objekts abzurufen.
4. Verwenden Sie die `Array.prototype.forEach()`-Methode, um über jede Eigenschaft zu iterieren und eine bereitgestellte Funktion auszuführen.
5. Die bereitgestellte Funktion sollte drei Argumente akzeptieren: den Eigenschaftswert, den Eigenschaftsschlüssel und das Objekt selbst.
6. Verwenden Sie die `forOwn()`-Funktion mit dem Objekt und der bereitgestellten Funktion, um über die Eigenschaften des Objekts zu iterieren.

Hier ist ein Beispielcodeausschnitt:

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

Dieser Code wird die Werte der `foo`- und `a`-Eigenschaften in der Konsole ausgeben.
