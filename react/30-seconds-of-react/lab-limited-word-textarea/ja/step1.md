# 単語制限付きのテキストエリア

> VM には既に `index.html` と `script.js` が提供されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

```jsx
// 単語制限付きのテキストエリアコンポーネントをレンダリングします。
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // 入力テキストをフォーマットするメモ化関数を作成します。
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // content の初期値に対して setFormattedContent を呼び出します。
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

変更内容：

- コードの各部分が何を行うかを説明するコメントを追加しました。
- `setFormattedContent` のロジックを単純化して、より簡潔にしました。
- `setContent` 関数を関数呼び出しの末尾に移動して、読みやすくしました。
- `<textarea>` コンポーネントの props を整列させて、一貫性を保ちました。
- 不要な空白と改行を削除しました。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
