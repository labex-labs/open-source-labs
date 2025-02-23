# Wie man in JavaScript rekursiv Objekte verschachtelt

Um Objekte in einem flachen Array rekursiv zu verschachteln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um Objekte, die miteinander verknüpft sind, zu verschachteln.
3. Verwenden Sie `Array.prototype.filter()`, um die Elemente zu filtern, bei denen die `id` mit der `link` übereinstimmt.
4. Verwenden Sie `Array.prototype.map()`, um jedes Element zu einem neuen Objekt zuzuordnen, das eine `children`-Eigenschaft hat, die die Elemente rekursiv basierend darauf verschachtelt, welche Kinder des aktuellen Elements sind.
5. Überspringen Sie das zweite Argument, `id`, um den Standardwert `null` zu verwenden, was angibt, dass das Objekt nicht mit einem anderen verknüpft ist (d.h. es ist ein oberstes Objekt).
6. Überspringen Sie das dritte Argument, `link`, um `'parent_id'` als Standard-Eigenschaft zu verwenden, die das Objekt mit einem anderen anhand seiner `id` verknüpft.

Hier ist der Code:

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

Um die `nest()`-Funktion zu verwenden, erstellen Sie ein Array von Objekten, die eine `id`-Eigenschaft und eine `parent_id`-Eigenschaft haben, die sie mit einem anderen Objekt verknüpft. Anschließend rufen Sie die `nest()`-Funktion auf und übergeben das Array als Argument. Die Funktion wird ein neues Array von Objekten zurückgeben, die basierend auf ihrer `parent_id`-Eigenschaft verschachtelt sind.

Beispiel:

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
