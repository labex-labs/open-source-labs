# 浮動セクション見出し付きのリスト

VM には既に `index.html` と `style.css` が用意されています。

各セクションに浮動見出し付きのリストを作成するには、次の手順に従ってください。

1. リストコンテナに `overflow-y: auto` を適用して、垂直方向のオーバーフローを許可します。
2. 内部コンテナ (`<dl>`) に `display: grid` を使用して、2 列のレイアウトを作成します。
3. 見出し (`<dt>`) を `grid-column: 1` に、コンテンツ (`<dd>`) を `grid-column: 2` に設定します。
4. 最後に、見出しに `position: sticky` と `top: 0.5rem` を適用して、浮動効果を作成します。

以下が HTML コードです。

```html
<div class="container">
  <div class="floating-stack">
    <dl>
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
      <dd>コンゴ共和国</dd>
      <dd>象牙海岸</dd>

      <dt>D</dt>
      <dd>ジブチ</dd>

      <dt>E</dt>
      <dd>エジプト</dd>
      <dd>赤道ギニア</dd>
      <dd>エリトリア</dd>
      <dd>エスワティニ（旧スワジランド）</dd>
      <dd>エチオピア</dd>
    </dl>
  </div>
</div>
```

以下が CSS コードです。

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0.5rem;
  left: 0.5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding: 0.25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0.75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0.25rem;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
