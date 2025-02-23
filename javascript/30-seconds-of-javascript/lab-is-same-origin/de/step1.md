# Überprüfen, ob zwei URLs von derselben Quelle stammen

Um zu überprüfen, ob zwei URLs von derselben Quelle stammen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie `URL.protocol` und `URL.host`, um zu überprüfen, ob beide URLs das gleiche Protokoll und den gleichen Host haben.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. Erstellen Sie zwei URL-Objekte mit den URLs, die Sie vergleichen möchten.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. Rufen Sie die `isSameOrigin`-Funktion mit den beiden URL-Objekten als Argumenten auf, um einen booleschen Ausgabewert zu erhalten.

```js
isSameOrigin(origin, destination); // true
```

5. Sie können die Funktion auch mit anderen URLs testen, um zu sehen, ob sie von derselben Quelle stammen oder nicht.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
