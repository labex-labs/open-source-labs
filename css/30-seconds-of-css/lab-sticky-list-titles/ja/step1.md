# 固定セクション ヘッダー付きのリスト

VM には既に `index.html` と `style.css` が用意されています。

各セクションに固定ヘッダー付きのリストを作成するには、次の手順に従います。

1. リスト コンテナ (`<dl>`) に対して、`overflow-y: auto` を使用して垂直方向のオーバーフローを許可します。
2. 見出し (`<dt>`) の `position` を `sticky` に設定し、`top: 0` を適用することで、コンテナの上部に固定します。
3. 次の HTML と CSS コードを使用します。

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
    <dt>A</dt>
    <dd>アルジェリア</dd>
    <dd>アンゴラ</dd>

    <dt>B</dt>
    <dd>ベニン</dd>
    <dd>ボツワナ</dd>
    <dd>ブルキナファソ</dd>
    <dd>ブルンジ</dd>

    <dt>C</dt>
    <dd>カーボベルデ</dd>
    <dd>カメルーン</dd>
    <dd>中央アフリカ共和国</dd>
    <dd>チャド</dd>
    <dd>コモロ</dd>
    <dd>民主主義人民共和国コンゴ</dd>
    <dd>共和国コンゴ</dd>
    <dd>コートジボワール</dd>

    <dt>D</dt>
    <dd>ジブチ</dd>

    <dt>E</dt>
    <dd>エジプト</dd>
    <dd>赤道ギニア</dd>
    <dd>エリトリア</dd>
    <dd>エスワティニ（元スワジランド）</dd>
    <dd>エチオピア</dd>
  </dl>
</div>
```

CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
