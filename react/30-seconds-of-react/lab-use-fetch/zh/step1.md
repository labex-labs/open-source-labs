# React 的 useFetch 钩子

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

以下是代码：

```jsx
const useFetch = (url, options) => {
  const [response, setResponse] = React.useState(null);
  const [error, setError] = React.useState(null);
  const [abort, setAbort] = React.useState(() => {});

  React.useEffect(() => {
    const abortController = new AbortController();
    const signal = abortController.signal;

    const fetchData = async () => {
      try {
        const res = await fetch(url, { ...options, signal });
        const json = await res.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();

    return () => {
      abort();
    };
  }, []);

  return { response, error, abort };
};

const ImageFetch = (props) => {
  const res = useFetch("https://dog.ceo/api/breeds/image/random", {});

  if (!res.response) {
    return <div>Loading...</div>;
  }

  const imageUrl = res.response.message;

  return (
    <div>
      <img src={imageUrl} alt="avatar" width={400} height="auto" />
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<ImageFetch />);
```

解释：

- 这段代码的目的是使用 React 钩子以声明式的方式实现一个 `fetch()` 调用。
- `useFetch` 钩子接受两个参数：一个 `url` 和一个 `options` 对象。
- 该钩子使用 `useState()` 钩子初始化三个状态变量：`response`、`error` 和 `abort`。
- `useEffect()` 钩子用于异步调用 `fetch()` 并相应地更新状态变量。
- `AbortController` 用于允许中止请求，并且在组件卸载时用于取消请求。
- 该钩子返回一个包含 `response`、`error` 和 `abort` 状态变量的对象。
- `ImageFetch` 组件使用 `useFetch` 钩子来获取一张随机的狗狗图片，并将其显示在一个 `<img>` 元素中。

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
