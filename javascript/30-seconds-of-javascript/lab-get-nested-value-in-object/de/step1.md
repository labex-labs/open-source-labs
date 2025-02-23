# Wie man einen geschachtelten Wert in einem JSON-Objekt erhält

Um einen Zielwert aus einem geschachtelten JSON-Objekt basierend auf einem angegebenen Schlüssel abzurufen, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Überprüfen Sie, ob das `target` im `obj` mithilfe des `in`-Operators vorhanden ist.
- Wenn das `target` gefunden wird, geben Sie den entsprechenden Wert im `obj` zurück.
- Wenn das `target` nicht gefunden wird, verwenden Sie `Object.values()` und `Array.prototype.reduce()`, um die `dig`-Funktion rekursiv auf jedes geschachtelte Objekt aufzurufen, bis das erste übereinstimmende Schlüssel/Wert-Paar gefunden ist.

Hier ist der Code für die `dig`-Funktion:

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

Um die `dig`-Funktion zu verwenden, erstellen Sie zunächst ein JSON-Objekt mit geschachtelten Ebenen, wie folgt:

```js
const data = {
  level1: {
    level2: {
      level3: "einige Daten"
    }
  }
};
```

Rufen Sie dann die `dig`-Funktion mit dem JSON-Objekt und dem gewünschten Schlüssel auf:

```js
dig(data, "level3"); // 'einige Daten'
dig(data, "level4"); // undefined
```

Diese Beispiele werden den Wert des `level3`-Schlüssels im `data`-Objekt zurückgeben und `undefined` für den nicht vorhandenen `level4`-Schlüssel.
