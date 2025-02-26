# React useNavigatorOnLine フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

クライアントがオンラインかオフラインかを確認するには、`Navigator.onLine` ウェブ API を利用する `getOnLineStatus` 関数を作成できます。そして、React コンポーネントでこの機能を実装するには、`useNavigatorOnLine` カスタムフックを使用できます。このフックは `useState()` フックを使って `status` という状態変数を作成し、それを `getOnLineStatus()` が返す値に設定します。`useEffect()` フックは、オンライン/オフライン状態が変化したときのイベントリスナーを追加し、それに応じて `status` 状態変数を更新し、コンポーネントがマウント解除されたときにそれらのリスナーをクリーンアップします。最後に、`useNavigatorOnLine()` が返す `isOnline` 変数を使って、クライアントがオンラインかオフラインかを示すメッセージをレンダリングできます。

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
