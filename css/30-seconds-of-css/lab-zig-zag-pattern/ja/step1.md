# ジグザグの背景パターン

VM 内には既に `index.html` と `style.css` が用意されています。

ジグザグの背景パターンを作成するには、次の手順を使用します。

1. `background-color` を使用して白色の背景を設定します。
2. 4 つの `linear-gradient()` 値を持つ `background-image` を使用して、ジグザグパターンの部分を作成します。
3. `background-size` を使用してパターンのサイズを指定します。
4. `background-position` を使用して、パターンの部分を正しい位置に配置します。
5. パターンを繰り返すには、`background-repeat` を使用します。
6. **注記**：要素の `height` と `width` は、示す目的だけのために固定されています。

以下はコードのサンプルです。

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%), linear-gradient(
      315deg,
      #000 25%,
      transparent 25%
    ), linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
