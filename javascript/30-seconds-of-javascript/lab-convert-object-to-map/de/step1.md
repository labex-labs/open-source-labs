# So wandelt man ein Objekt in eine Map um

Um ein Objekt in eine `Map` umzuwandeln, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Object.entries()`, um das Objekt in ein Array von Schlüssel-Wert-Paaren zu konvertieren.
3. Verwenden Sie den `Map`-Konstruktor, um das Array in eine `Map` zu konvertieren.

Hier ist ein Beispielcodeausschnitt:

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

Sie können die `objectToMap()`-Funktion verwenden, um ein Objekt in eine `Map` umzuwandeln. Beispiel:

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
