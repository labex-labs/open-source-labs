# 录制动画帧指南

要录制动画帧，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用递归在每个动画帧上调用提供的回调函数。
3. 如果 `running` 为 `true`，则继续调用 `Window.requestAnimationFrame()`，它会调用提供的回调函数。
4. 为了允许手动控制录制，返回一个包含 `start` 和 `stop` 两个方法的对象。
5. 省略第二个参数 `autoStart`，以便在调用函数时隐式调用 `start`。

使用以下代码录制动画帧：

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

代码的示例用法：

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// 在每个动画帧上记录 'Animation frame fired'
recorder.stop(); // 停止记录
recorder.start(); // 再次开始
const recorder2 = recordAnimationFrames(cb, false);
// 需要显式调用 `start` 才能开始记录帧
```
