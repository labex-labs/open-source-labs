# 文件拖放区域

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

此组件允许对单个文件进行拖放功能。要实现此组件，请执行以下步骤：

1. 创建一个名为 `dropRef` 的引用，并将其绑定到组件的包装器。
2. 使用 `useState()` 钩子创建 `drag` 和 `filename` 变量。分别将它们初始化为 `false` 和 `''`。
3. 变量 `dragCounter` 和 `drag` 用于确定文件是否正在被拖动，而 `filename` 用于存储拖放文件的名称。
4. 创建 `handleDrag`、`handleDragIn`、`handleDragOut` 和 `handleDrop` 方法来处理拖放功能。`handleDrag` 防止浏览器打开被拖动的文件，`handleDragIn` 和 `handleDragOut` 处理被拖动的文件进入和离开组件，`handleDrop` 处理文件被放下并将其传递给 `onDrop`。
5. 使用 `useEffect()` 钩子，使用先前创建的方法处理每个拖放事件。

以下是该组件的 CSS：

```css
.filedrop {
  min-height: 120px;
  border: 3px solid #d3d3d3;
  text-align: center;
  font-size: 24px;
  padding: 32px;
  border-radius: 4px;
}

.filedrop.drag {
  border: 3px dashed #1e90ff;
}

.filedrop.ready {
  border: 3px solid #32cd32;
}
```

以下是该组件的 JSX：

```jsx
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState("");
  const dropRef = React.useRef(null);
  let dragCounter = 0;

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    const div = dropRef.current;
    div.addEventListener("dragenter", handleDragIn);
    div.addEventListener("dragleave", handleDragOut);
    div.addEventListener("dragover", handleDrag);
    div.addEventListener("drop", handleDrop);
    return () => {
      div.removeEventListener("dragenter", handleDragIn);
      div.removeEventListener("dragleave", handleDragOut);
      div.removeEventListener("dragover", handleDrag);
      div.removeEventListener("drop", handleDrop);
    };
  }, []);

  return (
    <div
      ref={dropRef}
      className={
        drag ? "filedrop drag" : filename ? "filedrop ready" : "filedrop"
      }
    >
      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
    </div>
  );
};
```

要使用该组件，请调用 `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);`

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
