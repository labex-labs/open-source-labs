# React useCopyToClipboard フック

> VM には既に `index.html` と `script.js` が提供されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

指定されたテキストをクリップボードにコピーするには、`/js/s/copy-to-clipboard/` に提供されている `copyToClipboard` スニペットと `useState()` フックを使用して `copied` 変数を初期化します。`copyToClipboard` メソッドのコールバックを作成するには、`useCallback()` フックを使用します。`text` が変更されたときに `copied` 状態変数をリセットするには、`useEffect()` フックを使用します。最後に、`copied` 状態変数と `copy` コールバックを返します。

次のコードは、これらのフックとメソッドを使用して `TextCopy` コンポーネントを作成する方法の例を示しています。ユーザーが「クリックしてコピー」ボタンをクリックすると、`copy` 関数が呼び出され、`copied` 変数が `true` に設定されます。コピーが成功した場合、「コピー済み！」が表示されます。

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
