# Wie man die Ausführung einer Funktion in JavaScript verzögert

Um die Ausführung einer Funktion in JavaScript zu verzögern, kannst du die `setTimeout()`-Methode verwenden. Hier ist, wie man es macht:

1. Öffne das Terminal/SSH und tippe `node`, um mit der Codeausführung zu beginnen.
2. Verwende die folgende Syntax, um die Ausführung einer Funktion `fn` um `ms` Millisekunden zu verzögern:

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. Um Argumente an die Funktion zu übergeben, verwende den Spread (`...`)-Operator wie folgt:

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "later"
); // Gibt 'later' nach einer Sekunde aus.
```

Mit diesem Code wird die bereitgestellte Funktion `fn` nach der angegebenen Anzahl von Millisekunden (`ms`) aufgerufen. Der Parameter `...args` ermöglicht es dir, beliebig viele Argumente an die Funktion zu übergeben.
