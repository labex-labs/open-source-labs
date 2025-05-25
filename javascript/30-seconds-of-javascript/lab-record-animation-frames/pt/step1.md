# Guia para Gravar Quadros de Animação

Para gravar quadros de animação, siga os passos abaixo:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use recursão para invocar o callback fornecido em cada quadro de animação.
3. Se `running` for `true`, continue invocando `Window.requestAnimationFrame()`, que invoca o callback fornecido.
4. Para permitir o controle manual da gravação, retorne um objeto com dois métodos `start` e `stop`.
5. Omita o segundo argumento, `autoStart`, para chamar implicitamente `start` quando a função for invocada.

Use o seguinte código para gravar quadros de animação:

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

Exemplo de uso do código:

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// logs 'Animation frame fired' on each animation frame
recorder.stop(); // stops logging
recorder.start(); // starts again
const recorder2 = recordAnimationFrames(cb, false);
// `start` needs to be explicitly called to begin recording frames
```
