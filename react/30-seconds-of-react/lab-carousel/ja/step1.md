# キャルーセル

> VM 内には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

このコードはキャルーセルコンポーネントをレンダリングします。以下がその手順です：

1. `useState()` フックを使って `active` という状態変数を作成し、`0`（キャルーセル内の最初の項目のインデックス）で初期化します。
2. `useEffect()` フックを使って `setTimeout()` でタイマーを設定します。タイマーが発火すると、`active` の値をキャルーセル内の次の項目のインデックスに更新します（必要に応じて剰余演算子を使って先頭に戻ります）。また、コンポーネントがアンマウントされるときにタイマーをクリーンアップします。
3. 各キャルーセル項目に対して `className` を計算します。それは、項目が現在アクティブかどうかに基づいて適切なクラスを適用しながらマッピングすることで行われます。
4. `React.cloneElement()` を使ってキャルーセル項目をレンダリングし、`...rest` を使って任意の追加の props を渡し、各項目に計算された `className` を追加します。

CSS スタイルはキャルーセルとその項目のレイアウトを定義します。キャルーセルコンテナは `position: relative` で、項目はデフォルトで `position: absolute` かつ `visibility: hidden` になっています。項目がアクティブになると、`visible` クラスが付与され、`visibility` が `visible` に設定されます。

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

以下が完全なコードです：

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>carousel item 1</div>,
      <div>carousel item 2</div>,
      <div>carousel item 3</div>
    ]}
  />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
