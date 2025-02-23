# Das Klonen eines regulären Ausdrucks

Um einen regulären Ausdruck zu klonen, verwenden Sie den `RegExp`-Konstruktor, `RegExp.prototype.source` und `RegExp.prototype.flags`.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

Dieser Code erstellt eine Kopie des angegebenen regulären Ausdrucks. Beispiel:

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp!== regExp2
```
