# タブ

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

タブ付きメニューとビュー コンポーネントをレンダリングするには、次の手順に従います。

1. `Tabs` コンポーネントを定義します。`useState()` フックを使用して、`bindIndex` 状態変数を `defaultIndex` に設定します。
2. `TabItem` コンポーネントを定義し、`Tabs` コンポーネントに渡された `children` をフィルタリングして、`TabItem` 以外の不要なノードを削除します。これは、関数の名前を識別することで行うことができます。
3. `changeTab` と呼ばれる関数を定義します。この関数は、ユーザーがメニューから `<button>` をクリックしたときに実行されます。
4. `changeTab` は、渡されたコールバック `onTabClick` を実行し、クリックされた要素に基づいて `bindIndex` を更新します。
5. 収集されたノードに `Array.prototype.map()` を使用して、タブのメニューとビューをレンダリングします。
6. `bindIndex` の値を使用してアクティブなタブを決定し、正しい `className` を適用します。

以下は、タブ付きメニューとビューをスタイリッシュにするための CSS コードです。

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

以下は、`Tabs` コンポーネントを実装するための JavaScript コードです。

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

最後に、`Tabs` コンポーネントの使用例を示します。

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
