# Guide to Record Animation Frames

To record animation frames, follow the steps below:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion to invoke the provided callback on each animation frame.
3. If `running` is `true`, continue invoking `Window.requestAnimationFrame()`, which invokes the provided callback.
4. To allow manual control of the recording, return an object with two methods `start` and `stop`.
5. Omit the second argument, `autoStart`, to implicitly call `start` when the function is invoked.

Use the following code to record animation frames:

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

Example usage of the code:

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// logs 'Animation frame fired' on each animation frame
recorder.stop(); // stops logging
recorder.start(); // starts again
const recorder2 = recordAnimationFrames(cb, false);
// `start` needs to be explicitly called to begin recording frames
```
