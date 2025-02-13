# 个人作品集

首先，打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
│   ├── components
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
- `toggleVisible` 函数用于检查滚动位置，并相应地更新 `showBackToTopBtn` 状态。
- `useEffect` 钩子用于向窗口的滚动事件添加事件监听器，该事件会触发 `toggleVisible` 函数。
- `scrollToTop` 函数用于在点击返回顶部按钮时将窗口滚动到顶部。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![完成的项目演示](../assets/finished.gif)
