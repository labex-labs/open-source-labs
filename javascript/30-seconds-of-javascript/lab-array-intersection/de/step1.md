# Array-Schnittmenge finden

Um die gemeinsamen Elemente zwischen zwei Arrays zu finden und Duplikate zu entfernen, verwenden Sie folgenden Code:

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

Um diesen Code zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Rufen Sie dann die `intersection`-Funktion mit zwei Arrays als Argumenten auf, wie folgt:

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

Dies wird ein Array zurückgeben, das die Elemente enthält, die in beiden Arrays vorhanden sind, mit Duplikaten entfernt.
