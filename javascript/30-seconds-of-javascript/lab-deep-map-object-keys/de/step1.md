# Deep Map Object Keys

Um die Schlüssel eines Objekts tief zuzuordnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `deepMapKeys`-Funktion mit dem bereitgestellten Objekt und einer Funktion, die neue Schlüssel generiert.
3. Die Funktion erstellt ein Objekt mit denselben Werten wie das bereitgestellte Objekt und Schlüsseln, die durch Ausführen der bereitgestellten Funktion für jeden Schlüssel generiert werden.
4. Iterieren Sie über die Schlüssel des Objekts mithilfe von `Object.keys()`.
5. Erstellen Sie ein neues Objekt mit denselben Werten und zugeordneten Schlüsseln mithilfe von `Array.prototype.reduce()` und der bereitgestellten Funktion.
6. Wenn ein Wert ein Objekt ist, rufen Sie `deepMapKeys` rekursiv auf, um auch seine Schlüssel zuzuordnen.

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

Hier ist ein Beispiel für die Verwendung von `deepMapKeys`:

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
