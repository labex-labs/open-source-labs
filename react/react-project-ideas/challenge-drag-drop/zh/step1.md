# 拖放功能

首先，打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
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

- 请在 `App.js` 文件中完成此挑战。
- `onDragStart` 函数已定义。它是任务卡片上 `dragstart` 事件的事件处理程序。它将数据传输数据设置为任务的名称属性，该属性将用于在任务被放下时识别任务。
- `onDrop` 函数已定义。它是任务板上 `drop` 事件的事件处理程序。它从数据传输数据中检索任务的名称，根据放下位置（类别）更新任务状态中的任务类别，并使用 `setTasks` 设置更新后的任务状态。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![拖放演示](../assets/finished.gif)
