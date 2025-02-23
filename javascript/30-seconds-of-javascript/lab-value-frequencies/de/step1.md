# Anweisungen zur Zählung von Werthäufigkeiten

Um die Häufigkeit von Werten in einem Array zu zählen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Array.prototype.reduce()`-Methode, um die einzigartigen Werte auf die Schlüssel eines Objekts abzubilden und jedem vorhandenen Schlüssel jedes Mal, wenn derselbe Wert auftritt, hinzuzufügen. Dadurch wird ein Objekt erstellt, dessen Schlüssel die einzigartigen Werte des Arrays sind und dessen Werte die Häufigkeiten dieser Werte.
3. Der Code für diese Operation lautet wie folgt:

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4. Um diese Funktion zu verwenden, rufen Sie `frequencies` mit dem Array als Argument auf. Beispielsweise:

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

Mit diesen Anweisungen können Sie die Häufigkeit von Werten in jedem gegebenen Array leicht zählen.
