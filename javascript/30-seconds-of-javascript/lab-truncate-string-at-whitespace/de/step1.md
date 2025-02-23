# Wie man in JavaScript einen String an Leerzeichen abkürzt

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Funktion, die einen String bis zu einer bestimmten Länge abkürzt, wobei Leerzeichen so weit wie möglich beibehalten werden:

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

Um diese Funktion zu verwenden, übergeben Sie als erstes Argument den String, den Sie abkürzen möchten, als zweites Argument die maximale Länge und als drittes Argument einen optionalen Endstring. Wenn die Länge des Strings kleiner oder gleich der angegebenen Grenze ist, wird der ursprüngliche String zurückgegeben. Andernfalls sucht die Funktion den letzten Leerzeichen vor der Grenze und kürzt den String dort ab, wobei der Endstring hinzugefügt wird, wenn er angegeben ist.

Hier sind einige Beispiele:

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
