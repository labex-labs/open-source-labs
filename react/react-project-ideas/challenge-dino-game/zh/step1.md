# 恐龙游戏

首先，打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
│   ├──components
│   │  └── Dino
│   │       ├── img
│   │       │   ├── cactus.png
│   │       │   └── trex.png
│   │       ├── Dino.css
│   │       └── Dino.js
│   ├── App.js
│   ├── App.css
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

- 请在 `src/components/Dino/Dino.js` 文件中完成此挑战。
- 初始化两个 `useRef` 钩子：`dinoRef` 和 `cactusRef`。这些钩子将用于引用恐龙和仙人掌的 DOM 元素。
- 初始化一个名为 `score` 的 `useState` 钩子，初始值为 0。此钩子将跟踪玩家的分数。
- 定义 `jump` 函数。它将 “jump” 类添加到由 `dinoRef` 引用的恐龙 DOM 元素中。这会触发一个 CSS 动画，使恐龙跳跃。在 300 毫秒的超时后，“jump” 类被移除，恐龙回到其原始位置。
- 使用 `useEffect` 钩子来处理游戏逻辑。它设置一个每 10 毫秒运行一次的间隔。在间隔函数内部，它使用 `getComputedStyle` 函数获取恐龙（`dinoTop`）和仙人掌（`cactusLeft`）的当前位置。
- 它通过将仙人掌位置（`cactusLeft`）与恐龙位置（`dinoTop`）进行比较来检查是否发生碰撞。如果仙人掌在一定范围内且与恐龙高度相同，则检测到碰撞。在这种情况下，会显示一个包含玩家分数的警报，并使用 `setScore` 函数将分数重置为 0。否则，使用 `setScore` 将分数增加 1。
- 第一个 `useEffect` 钩子还返回一个清理函数，该函数在组件卸载时清除间隔。这可确保正确清理间隔以避免内存泄漏。
- 第二个 `useEffect` 钩子负责设置和移除 “keydown” 事件的事件监听器。当按下某个键时，调用 `jump` 函数。这允许玩家通过按下任意键使恐龙跳跃。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![恐龙游戏最终结果](../assets/finished.gif)
