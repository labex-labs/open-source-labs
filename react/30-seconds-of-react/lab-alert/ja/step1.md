# 閉じることができるアラート

> `index.html` と `script.js` はすでに仮想マシン（VM）に用意されています。一般的には、`script.js` と `style.css` にコードを追加するだけです。

`type` プロップを持つアラートコンポーネントをレンダリングします。

`Alert` コンポーネントは以下のプロップを受け取ります。

- `isDefaultShown`：アラートが最初に表示されるかどうかを決定するブール値（デフォルトは `false`）
- `timeout`：アラートがフェードアウトするまでの時間をミリ秒で指定する数値（デフォルトは `250`）
- `type`：アラートのタイプを決定する文字列（例："warning"、"error"、"info"）
- `message`：アラートに表示するメッセージを含む文字列

このコンポーネントは以下のことを行います。

- `useState()` フックを使用して `isShown` と `isLeaving` の状態変数を作成し、最初は両方とも `false` に設定します。
- コンポーネントがアンマウントされたときにタイマーをクリアするために、`timeoutId` 変数を定義してタイマーインスタンスを保持します。
- `useEffect()` フックを使用して、`isShown` の値を `true` に更新し、コンポーネントがアンマウントされたときに `timeoutId` を使用してインターバルをクリアします。
- `closeAlert` 関数を定義して、フェードアウトアニメーションを表示し、`setTimeout()` を介して `isShown` を `false` に設定することで、コンポーネントを DOM から削除するようにします。
- `isShown` が `true` の場合、アラートコンポーネントをレンダリングします。このコンポーネントは `type` プロップに基づいた適切なスタイルを持ち、`isLeaving` が `true` の場合はフェードアウトします。

以下がコードです。

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert.close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert.close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
