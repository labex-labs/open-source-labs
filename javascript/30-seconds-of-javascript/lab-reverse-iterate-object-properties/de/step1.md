# So geht man in umgekehrter Reihenfolge über die eigenen Eigenschaften eines Objekts iterieren

Um in umgekehrter Reihenfolge über die eigenen Eigenschaften eines Objekts zu iterieren und für jede eine Callback-Funktion auszuführen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Object.keys()`, um alle Eigenschaften des Objekts zu erhalten.
3. Verwenden Sie `Array.prototype.reverse()`, um die Reihenfolge der Eigenschaften umzukehren.
4. Verwenden Sie `Array.prototype.forEach()`, um die bereitgestellte Funktion für jedes Schlüssel-Wert-Paar auszuführen.
5. Die Callback-Funktion sollte drei Argumente haben: den Wert, den Schlüssel und das Objekt.

Hier ist der Code:

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

Sie können diese Funktion mit jedem Objekt und jeder Callback-Funktion verwenden. Beispielsweise können Sie den folgenden Code verwenden, um die Werte von `{ foo: 'bar', a: 1 }` in umgekehrter Reihenfolge auszugeben:

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
