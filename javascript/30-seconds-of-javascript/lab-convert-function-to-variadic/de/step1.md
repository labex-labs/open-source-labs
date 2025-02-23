# Umwandeln einer Funktion in eine variadische Funktion

Um eine Funktion, die ein Array akzeptiert, in eine variadische Funktion umzuwandeln, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Geben Sie eine Closure zurück, die alle Eingaben in eine array-akzeptierende Funktion sammelt.

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. Verwenden Sie die `collectInto`-Funktion, um eine Funktion in eine variadische Funktion umzuwandeln.

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (nach ca. 2 Sekunden)
```

Dadurch können Sie in Ihrer Funktion beliebig viele Argumente akzeptieren und sie in einem Array sammeln, um sie weiter zu verarbeiten.
