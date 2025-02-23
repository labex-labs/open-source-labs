# Umwandeln eines Formulars in ein Objekt

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Sie können eine Reihe von Formularelementen als Objekt kodieren, indem Sie die folgenden Schritte ausführen:

1. Verwenden Sie den `FormData`-Konstruktor, um das HTML-`form` in `FormData` umzuwandeln.
2. Konvertieren Sie das `FormData` in ein Array mit `Array.from()`.
3. Sammeln Sie das Objekt aus dem Array mit `Array.prototype.reduce()`.

Hier ist ein Beispielcodeausschnitt:

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

Um ein bestimmtes Formular zu konvertieren, können Sie die `formToObject`-Funktion aufrufen und das Formularelement als Argument übergeben:

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
