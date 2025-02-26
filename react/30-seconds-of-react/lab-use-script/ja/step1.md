# React useScript フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

外部スクリプトを動的に読み込むには、`useState()` フックを使用して、スクリプトの読み込み状態を格納する状態変数を作成します。次に、`useEffect()` フックを使用して、`src` が変更されるたびに、スクリプトの読み込みとアンロードのすべてのロジックを処理します。`src` 値が存在しない場合は、`status` を `'idle'` に設定して返します。`Document.querySelector()` を使用して、適切な `src` 値を持つ `<script>` 要素が存在するかどうかを確認します。関連する要素が存在しない場合は、`Document.createElement()` を使用して作成し、適切な属性を付与します。`data-status` 属性を使用して、スクリプトの状態を示す方法として、最初に `'loading'` に設定します。関連する要素が存在する場合は、初期化をスキップし、`data-status` 属性から `status` を更新します。これにより、重複する要素が作成されないようになります。`EventTarget.addEventListener()` を使用して、`'load'` と `'error'` イベントをリッスンし、`data-status` 属性と `status` 状態変数を更新することで処理します。最後に、コンポーネントがアンマウントされるときに、`Document.removeEventListener()` を使用して、要素にバインドされたすべてのリスナーを削除します。

以下は、`useScript` フックの例の実装です：

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

以下は、`useScript` フックの使用例です：

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

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
