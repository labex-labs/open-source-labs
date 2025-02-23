# Memoize-Funktion

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion gibt die memoisierte (zwischengespeicherte) Funktion zurück. Hier sind die Schritte, um diese Funktion zu verwenden:

1. Instanziieren Sie ein neues `Map`-Objekt, um einen leeren Cache zu erstellen.
2. Geben Sie eine Funktion zurück, die ein einzelnes Argument annimmt, das an die memoisierte Funktion übergeben wird. Bevor die Funktion ausgeführt wird, überprüfen Sie, ob das Ergebnis für diesen spezifischen Eingabewert bereits zwischengespeichert ist. Wenn ja, geben Sie das zwischengespeicherte Ergebnis zurück; andernfalls speichern Sie es und geben Sie es zurück.
3. Verwenden Sie das `function`-Schlüsselwort, um es der memoisierten Funktion zu ermöglichen, ihren `this`-Kontext gegebenenfalls zu ändern.
4. Legen Sie den `Cache` als Eigenschaft auf der zurückgegebenen Funktion fest, um auf ihn zugreifen zu können.

Hier ist der Code, der die Memoize-Funktion implementiert:

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

Um zu sehen, wie diese Funktion funktioniert, können Sie sie mit der `anagrams`-Funktion verwenden. Hier ist ein Beispiel:

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // dauert lange
anagramsCached("javascript"); // liefert fast sofort zurück, da es zwischengespeichert ist
console.log(anagramsCached.cache); // Die zwischengespeicherte Anagramme-Karte
```
