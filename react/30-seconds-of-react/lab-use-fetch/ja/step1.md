# React useFetch フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

以下がコードです。

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

解説:

- このコードの目的は、React フックを使って宣言的に `fetch()` 呼び出しを実装することです。
- `useFetch` フックは 2 つのパラメータを取ります。`url` と `options` オブジェクトです。
- このフックは `useState()` フックを使って 3 つの状態変数を初期化します。`response`、`error`、および `abort` です。
- `useEffect()` フックは非同期で `fetch()` を呼び出し、それに応じて状態変数を更新するために使われます。
- `AbortController` は要求を中止するために使われ、コンポーネントがアンマウントされたときに要求をキャンセルするために使われます。
- このフックは `response`、`error`、および `abort` の状態変数を含むオブジェクトを返します。
- `ImageFetch` コンポーネントは `useFetch` フックを使ってランダムな犬の画像を取得し、`<img>` 要素に表示します。

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
