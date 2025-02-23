# Guía para registrar fotogramas de animación

Para registrar los fotogramas de una animación, siga los pasos siguientes:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la recursividad para llamar a la devolución de llamada proporcionada en cada fotograma de animación.
3. Si `running` es `true`, siga llamando a `Window.requestAnimationFrame()`, que llama a la devolución de llamada proporcionada.
4. Para permitir el control manual de la grabación, devuelva un objeto con dos métodos `start` y `stop`.
5. Omita el segundo argumento, `autoStart`, para llamar implícitamente a `start` cuando se invoque la función.

Utilice el siguiente código para registrar los fotogramas de una animación:

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

Uso de ejemplo del código:

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// muestra 'Animation frame fired' en cada fotograma de animación
recorder.stop(); // detiene la visualización
recorder.start(); // comienza de nuevo
const recorder2 = recordAnimationFrames(cb, false);
// se debe llamar explícitamente a `start` para comenzar a registrar los fotogramas
```
