# Den Datum von Gestern im Format yyyy-mm-dd erhalten

Um das Datum von gestern im Format `yyyy-mm-dd` zu erhalten, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Verwenden Sie den `Date`-Konstruktor, um das aktuelle Datum zu erhalten.
3. Verringern Sie das Datum um eins, indem Sie `Date.prototype.getDate()` verwenden.
4. Legen Sie das verringerte Datum fest, indem Sie `Date.prototype.setDate()` verwenden.
5. Verwenden Sie `Date.prototype.toISOString()`, um einen String im Format `yyyy-mm-dd` zurückzugeben.
6. Rufen Sie die Funktion `yesterday()` auf, um das Datum von gestern zu erhalten.

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // gibt "2018-10-17" zurück (wenn das aktuelle Datum 2018-10-18 ist)
```

Indem Sie diese Schritte befolgen, können Sie das Datum von gestern auf eine klare und prägnante Weise abrufen.
