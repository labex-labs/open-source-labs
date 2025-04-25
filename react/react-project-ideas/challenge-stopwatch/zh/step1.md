# 秒表

首先，打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
│   ├── components
│   │   ├──common
│   │   ├── stopwatch
│   │   ├── timer
│   │   ├── App.css
│   │   └── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## 要求

- 要安装项目依赖项，请使用以下命令：

  ```bash
  npm i
  ```

- 请在 `src/components/timer/Timer.js` 文件中完成此挑战。
- `onStart` 函数每秒由 `useEffect` 钩子调用一次。
  - 它检查计时器是否已达到 0 小时、0 分钟和 0 秒。如果是，则将 `isStarted` 设置为 `false` 并返回。
  - 如果计时器未启动，则不做任何更改直接返回。
  - 如果计时器正在运行，则将计时器减 1 秒。
  - 如果分钟或秒数达到 0，则使用 `setTimer` 函数相应地调整小时、分钟或秒数。
- `onReset` 函数在点击“重置”按钮时被调用。
  - 它将 `isStarted` 设置为 `false`，并将计时器重置为 0 小时、0 分钟和 0 秒。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![Finished stopwatch demonstration](../assets/finished.gif)
