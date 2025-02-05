# React useScript 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要动态加载外部脚本，请使用 `useState()` 钩子创建一个状态变量，用于存储脚本的加载状态。接下来，使用 `useEffect()` 钩子在 `src` 发生变化时处理加载和卸载脚本的所有逻辑。如果没有 `src` 值，将 `status` 设置为 `'idle'` 并返回。使用 `Document.querySelector()` 检查是否存在具有适当 `src` 值的 `<script>` 元素。如果不存在相关元素，则使用 `Document.createElement()` 创建一个并赋予其适当的属性。使用 `data-status` 属性来指示脚本的状态，初始时将其设置为 `'loading'`。如果存在相关元素，则跳过初始化并根据其 `data-status` 属性更新 `status`。这可确保不会创建重复的元素。使用 `EventTarget.addEventListener()` 监听 `'load'` 和 `'error'` 事件，并通过更新 `data-status` 属性和 `status` 状态变量来处理它们。最后，当组件卸载时，使用 `Document.removeEventListener()` 移除绑定到该元素的任何监听器。

以下是 `useScript` 钩子的示例实现：

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

以下是 `useScript` 钩子的示例用法：

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
