# Die Basis-URL abrufen

Um die Basis-URL aus einer gegebenen URL abzurufen, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH.
2. Tippen Sie `node`, um mit der Codeausübung zu beginnen.
3. Verwenden Sie die folgende JavaScript-Funktion, um die aktuelle URL ohne Parameter oder Fragmentidentifikatoren zu erhalten:

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. Ersetzen Sie `url` durch die URL, aus der Sie die Basis-URL abrufen möchten.
5. Die Funktion entfernt alles, was sich nach `'?'` oder `'#'` befindet, wenn gefunden, und gibt die Basis-URL zurück.
6. Hier ist ein Beispiel:

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
