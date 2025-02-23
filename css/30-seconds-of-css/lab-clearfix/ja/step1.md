# clearfix

VM 内には既に `index.html` と `style.css` が用意されています。

レイアウトを構築する際に `float` を使用する場合、要素がその子要素を自動的にクリアするようにするには、`::after` 疑似要素を使用して `content: ''` を適用してレイアウトに影響を与えさせます。また、`clear: both` を使用して要素が左と右の両方のフロートをクリアするようにします。ただし、このテクニックは、コンテナに非フロートの子要素がなく、クリアフィックスされたコンテナの前に同じフォーマットコンテキスト（たとえば、フロートされた列）内に高さのあるフロートがない場合にのみ正常に機能します。たとえば：

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

レイアウトを構築する際には、`float` を使用するよりも、フレックスボックスやグリッドレイアウトなどのより現代的なアプローチを使用することをお勧めします。

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
