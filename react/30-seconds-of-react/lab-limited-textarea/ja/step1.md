# 文字数制限付きのテキストエリア

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

以下がコードです。

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

このコードでは、以下のことを行っています。

- コメントを簡略化して、コードの各部分が何を行っているかをより簡潔にまとめました。
- 不要なコードコメントを削除しました。
- `useCallback`の依存配列から`setContent`関数を削除しました。それは必要ないからです。
- `useCallback`関数内の`text`引数の周りに丸括弧を追加して、一貫性を保ちました。
- 簡潔にするために、`onChange`イベントハンドラにアロー関数を使用しました。

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
