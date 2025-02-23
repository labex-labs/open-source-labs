# Wie man in JavaScript die Schlüssel von Objekten in Symbole umwandelt

Um in JavaScript die Schlüssel von Objekten in Symbole umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Object.keys()`-Methode, um die Schlüssel des Objekts zu erhalten, das Sie in ein Symbol umwandeln möchten.
3. Verwenden Sie die `Array.prototype.reduce()`-Methode und `Symbol`, um ein neues Objekt zu erstellen, bei dem jeder Schlüssel in ein `Symbol` umgewandelt wird.
4. Hier ist ein Beispielcodeausschnitt:

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5. Um die Funktion zu testen, rufen Sie `symbolizeKeys()` mit Ihrem Objekt als Argument auf, wie folgt:

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

Indem Sie diese Schritte befolgen, können Sie die Schlüssel jedes Objekts in JavaScript leicht in Symbole umwandeln.
