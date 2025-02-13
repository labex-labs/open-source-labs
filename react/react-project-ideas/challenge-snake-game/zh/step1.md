# 贪吃蛇游戏

首先，打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
│   ├── components
│   │   ├── Food.js
│   │   └── Snake.js
│   ├── App.css
│   ├── App.js
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

- 请在 `src/App.js` 文件中完成此挑战。
- `randomFoodPosition` 函数用于在游戏板上为食物生成随机位置。
- 在 `App` 函数内部，使用 `useState` 钩子定义了几个状态变量：
  - `snake` 表示蛇的当前状态。
  - `lastDirection` 表示蛇最后移动的方向。
  - `foodPosition` 表示食物的当前位置。
  - `isStarted` 确定游戏是否已开始。
  - `gameOver` 表示游戏是否结束。
  - `playgroundRef` 是对游戏板元素的引用。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![Snake game final result](../assets/finished.gif)
