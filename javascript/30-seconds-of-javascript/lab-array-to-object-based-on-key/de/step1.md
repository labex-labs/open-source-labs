# Umwandeln eines Arrays in ein Objekt basierend auf einem bestimmten Schlüssel

Um ein Array in ein Objekt basierend auf einem bestimmten Schlüssel umzuwandeln und diesen Schlüssel von jedem Wert auszuschließen, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Verwenden Sie `Array.prototype.reduce()`, um aus dem bereitgestellten Array ein Objekt zu erstellen.
- Verwenden Sie die Objektzerlegung, um den Wert des angegebenen `Schlüssels` und die zugehörigen `Daten` zu extrahieren und fügen Sie dann das Schlüssel-Wert-Paar zum Objekt hinzu.

Hier ist eine Beispielimplementierung:

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

Sie können die Funktion dann wie folgt verwenden:

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
