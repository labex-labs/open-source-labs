# Wie man zirkuläre JSON-Daten in einen String umwandelt

Um ein JSON-Objekt, das zirkuläre Referenzen enthält, in einen String umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie einen `WeakSet`, um bereits besuchte Werte zu speichern und zu überprüfen, indem Sie `WeakSet.prototype.add()` und `WeakSet.prototype.has()` verwenden.
3. Verwenden Sie `JSON.stringify()` mit einer benutzerdefinierten Ersetzungsmethode, die Werte, die bereits in `seen` vorhanden sind, überspringt und neue Werte gegebenenfalls hinzufügt.
4. ⚠️ **ACHTUNG:** Diese Funktion findet und entfernt zirkuläre Referenzen, was zu einem Datenverlust zirkulärer Daten im serialisierten JSON führt.

Hier ist der Code für die `stringifyCircularJSON`-Funktion:

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

Um die Funktion zu testen, können Sie ein Objekt mit einer zirkulären Referenz erstellen und `stringifyCircularJSON` aufrufen:

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
