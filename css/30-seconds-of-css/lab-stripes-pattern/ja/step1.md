# 縞模様の背景パターン

VM には既に `index.html` と `style.css` が用意されています。

このコードは、白い背景に垂直な縞模様を作成します。

パターンを作成するには：

- `background-color` プロパティを白に設定します。
- `background-image` に `linear-gradient()` 値を使用して垂直な縞を作成します。
- `background-size` プロパティを設定して各縞のサイズを指定します。
- `background-repeat` を `repeat` に設定して、パターンが要素を埋めるようにします。

要素の固定された `width` と `height` は、示すためだけのものであることに注意してください。

以下はコードの例です：

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
