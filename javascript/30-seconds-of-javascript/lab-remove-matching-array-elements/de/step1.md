# Entfernen von übereinstimmenden Elementen aus einem Array

Um bestimmte Elemente aus einem Array basierend auf einer gegebenen Bedingung zu entfernen, können Sie die `remove`-Funktion verwenden. Diese Funktion verändert das ursprüngliche Array, indem sie Elemente entfernt, für die die gegebene Funktion `false` zurückgibt.

Hier sind die Schritte, um die `remove`-Funktion zu verwenden:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.filter()`, um Arrayelemente zu finden, die wahrheitswerte zurückgeben.
3. Verwenden Sie `Array.prototype.reduce()`, um Elemente mit `Array.prototype.splice()` zu entfernen.
4. Die Callback-Funktion wird mit drei Argumenten (Wert, Index, Array) aufgerufen.

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

Hier ist ein Beispiel für die Verwendung der `remove`-Funktion:

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

Dies wird ein neues Array mit den entfernten Elementen zurückgeben.
