# 折りたたみ可能なコンテンツ

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加する必要があります。

この関数は、コンテンツの表示を切り替えるボタン付きの折りたたみ可能なコンポーネントをレンダリングします。使い方は以下の通りです。

1. `useState()`フックを使って、コンテンツが現在折りたたまれているか展開されているかを表す`isCollapsed`という状態変数を作成します。初期値は`collapsed`に設定します。
2. `<button>`要素を使って`isCollapsed`の状態を切り替え、`children`プロップを通じて渡されたコンテンツを表示/非表示にします。
3. `isCollapsed`を使って、コンテンツコンテナに`collapsed`または`expanded`の適切な CSS クラスを適用し、その外見を決定します。
4. コンテンツコンテナの`aria-expanded`属性を`isCollapsed`の状態に基づいて更新し、障害者向けにコンポーネントをアクセス可能にします。

このコンポーネントに必要な CSS コードは以下の通りです。

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

そして JavaScript コードは以下の通りです。

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Show" : "Hide"} content
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

このコンポーネントを使うには、折りたたみたいコンテンツを渡して簡単に呼び出します。

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>This is a collapse</h1>
    <p>Hello world!</p>
  </Collapse>
);
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080**タブを更新して Web ページをプレビューできます。
