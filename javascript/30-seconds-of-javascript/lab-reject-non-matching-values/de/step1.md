# Das Filtern von Array-Werten

Um ein Array anhand einer Prädikatsfunktion zu filtern und nur die Werte zurückzugeben, für die die Prädikatsfunktion `false` zurückgibt, folgen Sie diesen Schritten:

1. Verwenden Sie `Array.prototype.filter()` in Kombination mit der Prädikatsfunktion `pred`.
2. Die Filter-Methode wird nur die Werte zurückgeben, für die die Prädikatsfunktion `false` zurückgibt.
3. Um nicht übereinstimmende Werte abzulehnen, übergeben Sie die Prädikatsfunktion und das Array an die `reject()`-Funktion.

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

Hier sind einige Beispiele dafür, wie die `reject()`-Funktion verwendet werden kann:

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

Indem Sie diese Schritte befolgen, können Sie ein Array leicht anhand einer Prädikatsfunktion filtern und nicht übereinstimmende Werte abweisen.
