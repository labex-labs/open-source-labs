# 星評価

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

親コンポーネントの状態に基づいて適切な外観で個々の星をレンダリングする `Star` コンポーネントを作成します。次に、`useState()` フックを使用して適切な初期値で `rating` と `selection` の状態変数を定義する `StarRating` コンポーネントを定義します。

`StarRating` では、提供された `event` に応じて `selection` を更新する `hoverOver` というメソッドを作成します。`event` が提供されないか、または `null` の場合、`selection` を `0` にリセットします。イベントのターゲットの `.data-star-id` 属性を使用して `selection` の値を決定します。

次に、`Array.from()` を使用して 5 つの要素の配列を作成し、`Array.prototype.map()` を使用して個々の `<Star>` コンポーネントを作成します。ラッピング要素の `onMouseOver` と `onMouseLeave` イベントを `hoverOver` を使って処理します。`onClick` イベントを `setRating` を使って処理します。

```css
.star {
  color: #ff9933;
  cursor: pointer;
}
```

```jsx
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? "\u2605" : "\u2606"}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = (event) => {
    let val = 0;
    if (event && event.target && event.target.getAttribute("data-star-id"))
      val = event.target.getAttribute("data-star-id");
    setSelection(val);
  };

  return (
    <div
      onMouseLeave={() => hoverOver(null)}
      onMouseOver={hoverOver}
      onClick={(e) =>
        setRating(e.target.getAttribute("data-star-id") || rating)
      }
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

最後に、`ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);` を呼び出すことで初期値 `2` で `StarRating` コンポーネントをレンダリングします。

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
