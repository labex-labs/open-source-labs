# Wie man in JavaScript ein Objekt in ein Array abbildet

Um in JavaScript ein Objekt in ein Array abzubilden, kannst du die `listify()`-Funktion verwenden. Hier ist, wie du es tun kannst:

1. Öffne das Terminal/SSH und tippe `node`, um zu beginnen, zu programmieren.

2. Verwende `Object.entries()`, um ein Array der Schlüssel-Wert-Paare des Objekts zu erhalten.

3. Verwende `Array.prototype.reduce()`, um das Array in ein Objekt abzubilden.

4. Verwende `mapFn`, um die Schlüssel und Werte des Objekts abzubilden, und `Array.prototype.push()`, um die abgebildeten Werte zum Array hinzuzufügen.

Hier ist der Code für die `listify()`-Funktion:

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

Und hier ist ein Beispiel, wie du es mit einem Objekt namens `people` verwendest:

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

Mit dieser Funktion kannst du in JavaScript leicht ein Objekt in ein Array abbilden.
