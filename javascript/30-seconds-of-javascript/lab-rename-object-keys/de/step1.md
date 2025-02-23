# Wie man in JavaScript die Schlüssel von Objekten umbenennt

Um mehrere Objekt-Schlüssel mit den bereitgestellten Werten umzubenennen, können Sie die `renameKeys`-Funktion verwenden. Hier sind die Schritte, die Sie befolgen müssen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Object.keys()` in Kombination mit `Array.prototype.reduce()` und dem Spread-Operator (`...`), um die Schlüssel des Objekts zu erhalten und sie gemäß `keysMap` umzubenennen.
3. Übergeben Sie die `keysMap` und das Objekt (`obj`) als Argumente an die `renameKeys`-Funktion.
4. Die `renameKeys`-Funktion gibt ein neues Objekt mit den umbenannten Schlüsseln zurück.

Hier ist ein Beispiel, wie die `renameKeys`-Funktion verwendet werden kann:

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
