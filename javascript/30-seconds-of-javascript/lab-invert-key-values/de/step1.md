# Funktion zum Umkehren eines Objekts

Um die Schlüssel-Wert-Paare eines Objekts umzukehren, ohne das ursprüngliche Objekt zu verändern, verwenden Sie die `invertKeyValues`-Funktion.

- Rufen Sie die Funktion auf, indem Sie `invertKeyValues(obj, fn)` in der Konsole/SSH eingeben, wobei `obj` das zu invertierende Objekt und `fn` eine optionale Funktion ist, die auf den umgekehrten Schlüssel angewendet werden soll.

- Die `Object.keys()`-Methode und `Array.prototype.reduce()` werden verwendet, um ein neues Objekt mit umgekehrten Schlüssel-Wert-Paaren zu erstellen, und wenn eine Funktion angegeben ist, wird sie auf jeden umgekehrten Schlüssel angewendet.

- Wenn `fn` weggelassen wird, gibt die Funktion nur die umgekehrten Schlüssel zurück, ohne dass auf sie eine Funktion angewendet wird.

- Die Funktion gibt ein Objekt zurück, bei dem jeder umgekehrte Wert ein Array von Schlüsseln ist, die für das Generieren des umgekehrten Werts verantwortlich sind.

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

Beispielverwendung:

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
