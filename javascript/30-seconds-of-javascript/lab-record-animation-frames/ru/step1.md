# Руководство по записи кадров анимации

Для записи кадров анимации следуйте шагам ниже:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте рекурсию для вызова предоставленного обратного вызова на каждом кадре анимации.
3. Если `running` имеет значение `true`, продолжайте вызывать `Window.requestAnimationFrame()`, которое вызывает предоставленный обратный вызов.
4. Чтобы позволить вручную управлять записью, верните объект с двумя методами `start` и `stop`.
5. Игнорируйте второй аргумент, `autoStart`, чтобы неявно вызвать `start` при вызове функции.

Используйте следующий код для записи кадров анимации:

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

Пример использования кода:

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// выводит 'Animation frame fired' на каждом кадре анимации
recorder.stop(); // останавливает вывод
recorder.start(); // начинает вывод снова
const recorder2 = recordAnimationFrames(cb, false);
// нужно явно вызвать `start`, чтобы начать запись кадров
```
