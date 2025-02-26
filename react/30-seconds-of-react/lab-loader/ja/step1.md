# スピニングローダー

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

**スピニングローダーコンポーネントをレンダリングします。**

スピニングローダーコンポーネントをレンダリングするには、次の手順に従います。

1. `size` プロップによってサイズが決定される SVG 要素をレンダリングします。
2. CSS を使って SVG をアニメーション化し、回転アニメーションを作成します。具体的には、SVG に `.loader` クラスを追加し、`animation` プロパティを `rotate 2s linear infinite` に設定します。また、`rotate` キーフレームを定義し、`transform` プロパティを使って SVG を 360 度回転させます。
3. 回転する円を表す `circle` 要素を SVG に追加します。円をアニメーション化するには、`.loader circle` セレクタを追加し、`animation` プロパティを `dash 1.5s ease-in-out infinite` に設定します。また、`dash` キーフレームを定義し、`stroke-dasharray` と `stroke-dashoffset` プロパティを使って、円の周りを移動する破線のストロークパターンを作成します。
4. 最後に、`size` プロップを幅と高さの属性として渡して SVG をレンダリングする `Loader` コンポーネントを作成します。

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

サイズが 24 の `Loader` コンポーネントを使用するには、`ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);` を呼び出します。

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
