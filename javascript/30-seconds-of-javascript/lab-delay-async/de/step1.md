# Wie man die Ausführung einer asynchronen Funktion in JavaScript verzögert

Um die Ausführung einer asynchronen Funktion in JavaScript zu verzögern, kannst du die untenstehende `sleep`-Funktion verwenden, die ein `Promise` zurückgibt, das nach einer bestimmten Zeit aufgelöst wird. Hier ist ein Beispiel dafür, wie man die Ausführung eines Teils einer `async`-Funktion mit `sleep` verzögert:

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("Ich werde für 1 Sekunde schlafen.");
  await sleep(1000);
  console.log("Ich bin nach 1 Sekunde aufgewacht.");
}
```

Um diese Funktion zu verwenden, rufe einfach `sleepyWork()` auf, und die Konsole wird die Nachrichten mit einer Verzögerung von 1 Sekunde zwischen ihnen ausgeben.
