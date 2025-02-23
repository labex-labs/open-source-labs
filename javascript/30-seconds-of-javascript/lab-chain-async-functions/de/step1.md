# Asynchrone Funktionen verketten

Um asynchrone Funktionen zu verketten, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dann iterieren Sie durch ein Array von Funktionen, die asynchrone Ereignisse enthalten, und rufen Sie die `next`-Funktion auf, wenn jedes asynchrone Ereignis abgeschlossen ist.

Hier ist ein Codeausschnitt, der zeigt, wie man asynchrone Funktionen verketten kann:

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 Sekunden");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 Sekunde");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 Sekunden");
  }
]);
```
