# Anleitung zum Aufzeichnen von Animationsframes

Um Animationsframes aufzunehmen, folgen Sie den Schritten unten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um den bereitgestellten Callback für jedes Animationsframe aufzurufen.
3. Wenn `running` `true` ist, rufen Sie fortlaufend `Window.requestAnimationFrame()` auf, was den bereitgestellten Callback aufruft.
4. Um die manuelle Steuerung der Aufzeichnung zu ermöglichen, geben Sie ein Objekt mit zwei Methoden `start` und `stop` zurück.
5. Überspringen Sie das zweite Argument, `autoStart`, um `start` implizit aufzurufen, wenn die Funktion aufgerufen wird.

Verwenden Sie den folgenden Code, um Animationsframes aufzunehmen:

```js
const recordAnimationFrames = (callback, autoStart = true) => {
  let running = false,
    raf;
  const stop = () => {
    if (!running) return;
    running = false;
    cancelAnimationFrame(raf);
  };
  const start = () => {
    if (running) return;
    running = true;
    run();
  };
  const run = () => {
    raf = requestAnimationFrame(() => {
      callback();
      if (running) run();
    });
  };
  if (autoStart) start();
  return { start, stop };
};
```

Beispielverwendung des Codes:

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// protokolliert 'Animation frame fired' für jedes Animationsframe
recorder.stop(); // stoppt das Protokollieren
recorder.start(); // startet erneut
const recorder2 = recordAnimationFrames(cb, false);
// `start` muss explizit aufgerufen werden, um die Frameaufzeichnung zu beginnen
```
