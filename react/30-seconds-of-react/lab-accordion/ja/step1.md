# 折りたたみ可能なアコーディオン

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

複数の折りたたみ可能なコンテンツ要素を持つアコーディオンメニューをレンダリングするには、次の手順を辿ることができます。

1. `<button>`をレンダリングし、`handleClick`コールバックを介して親に通知しながらコンポーネントを更新する`AccordionItem`コンポーネントを定義します。
2. `AccordionItem`内の`isCollapsed`プロップを使用してその外見を決定し、`className`を設定します。
3. `Accordion`コンポーネントを定義し、`useState()`フックを使用して`bindIndex`状態変数の値を`defaultIndex`に初期化します。
4. 関数の名前を識別することで、不必要なノードを除外し、`AccordionItem`以外の`children`をフィルタリングします。
5. 収集したノードに`Array.prototype.map()`を使用して個々の折りたたみ可能な要素をレンダリングします。
6. `AccordionItem`の`<button>`をクリックしたときに実行される`changeItem`を定義します。
7. `changeItem`は渡されたコールバック`onItemClick`を実行し、クリックされた要素に基づいて`bindIndex`を更新します。

以下はコードです。

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
