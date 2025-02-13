# 技能输入

首先，打开编辑器。你可以在编辑器中看到以下文件。

```txt
├── public
├── src
│   ├── components
│   │   └── TagInput.js
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

- 请在 `src/component/TagInput.js` 文件中完成此挑战。
- 当在输入字段中按下某个键时，会调用 `handleAddTag` 函数。如果按下的不是回车键，该函数会提前返回，不执行任何操作。否则，它会检查输入值，如果输入值不为空且尚未添加，则将其添加到标签状态中。然后，它会清空输入字段。
- 当点击某个标签时，会调用 `onDeleteTag` 函数。它会过滤标签状态以删除被点击的标签，并用过滤后的标签更新状态。

## 示例

完成代码后，使用以下命令运行它：

```bash
npm start
```

最终结果如下：

![Tag input functionality demo](../assets/finished.gif)
