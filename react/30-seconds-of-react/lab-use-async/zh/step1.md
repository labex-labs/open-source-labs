# React useAsync 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这段代码创建了一个处理异步调用的自定义钩子。它接受一个处理函数 `fn`，并返回一个包含 `state` 属性（`value`、`error` 和 `loading`）以及一个异步 `run` 函数的对象。`run` 函数运行提供的回调函数 `fn`，同时根据需要使用 `dispatch` 来更新 `state`。

```jsx
const useAsync = (fn) => {
  const initialState = { loading: false, error: null, value: null };

  const stateReducer = (state, action) => {
    switch (action.type) {
      case "start":
        return { loading: true, error: null, value: null };
      case "finish":
        return { loading: false, error: null, value: action.value };
      case "error":
        return { loading: false, error: action.error, value: null };
      default:
        return state;
    }
  };

  const [state, dispatch] = React.useReducer(stateReducer, initialState);

  const run = async (args = null) => {
    try {
      dispatch({ type: "start" });
      const value = await fn(args);
      dispatch({ type: "finish", value });
    } catch (error) {
      dispatch({ type: "error", error });
    }
  };

  return { ...state, run };
};

const RandomImage = (props) => {
  const imgFetch = useAsync((url) =>
    fetch(url).then((response) => response.json())
  );

  return (
    <div>
      <button
        onClick={() => imgFetch.run("https://dog.ceo/api/breeds/image/random")}
        disabled={imgFetch.loading}
      >
        加载图片
      </button>
      <br />
      {imgFetch.loading && <div>加载中...</div>}
      {imgFetch.error && <div>错误 {imgFetch.error}</div>}
      {imgFetch.value && (
        <img
          src={imgFetch.value.message}
          alt="头像"
          width={400}
          height="auto"
        />
      )}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<RandomImage />);
```

请点击右下角的“启动实时服务器”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
