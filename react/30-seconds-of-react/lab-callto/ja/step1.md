# 呼び出し可能な電話リンク

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

電話番号を呼び出すリンクを作成するには、`Callto` コンポーネントを使用します。このコンポーネントは、適切な `href` 属性を持つ `<a>` 要素を作成します。リンクをレンダリングするには、`phone` プロップを使って電話番号を指定し、`children` プロップを使ってリンクのテキストを指定します。

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

`Callto` コンポーネントを使用するには、`ReactDOM.render()` メソッドを呼び出し、`phone` と `children` プロップが設定された `Callto` 要素を渡します。

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Call me!</Callto>,
  document.getElementById("root")
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
