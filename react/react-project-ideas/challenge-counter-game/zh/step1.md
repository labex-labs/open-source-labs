# 计数器游戏

要开始，请打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
│   ├── components
│   │  └── HomePage
│   │       ├── HomePage.css
│   │       └── HomePage.js
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

- 请在 `components/HomePage/HomePage.js` 文件中完成此挑战。
- 使用 `useState` 钩子定义两个状态变量：`count` 和 `timer`。
- 使用 `useEffect` 钩子在定时器状态变量发生变化时启动定时器。
- 检查 `timer` 的值。如果为零，则该效果提前返回，不执行任何操作。
- 如果 `timer` 的值不为零，则设置一个时间间隔，每秒（1000 毫秒）将 `timer` 的值减 1。
- 返回一个清理函数，该函数在组件卸载或定时器值发生变化时清除时间间隔。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![Finished counter game demo](../assets/finished.gif)
